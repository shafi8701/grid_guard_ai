import json
import ollama
from domain.models.request import ComplianceRequest


def get_llm_response(request: ComplianceRequest):

    prompt = f"""
    You are a compliance and pricing expert.

    Product: {request.product}
    Region: {request.region}
    Price: {request.price}
    Certifications: {request.certifications}

    Return ONLY JSON:
    {{
        "allowed": boolean,
        "region": "{request.region}",
        "conditions": [],
        "reason": "",
        "pricing_compliance": "VALID or INVALID",
        "risk_level": "LOW or MEDIUM or HIGH"
    }}
    """

    try:
        response = ollama.chat(
            model="llama3",
            host="http://ollama:11434",
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ]
        )

        output_text = response['message']['content']

        output_text = output_text.strip().replace("```json", "").replace("```", "")

        return json.loads(output_text)

    except Exception as e:
        return {
            "allowed": False,
            "region": request.region,
            "conditions": [],
            "reason": f"Ollama failed: {str(e)}",
            "pricing_compliance": "INVALID",
            "risk_level": "HIGH"
        }