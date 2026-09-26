import json, sys
from client import AdversarialPromptJailbreakDetectorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "adversarial-prompt-jailbreak-detector", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "detect_jailbreak_attempt", "description": "Detects adversarial prompt injection, DAN exploits, and multi-vector jailbreak circumventions."}]}}
    elif method == "tools/call":
        client = AdversarialPromptJailbreakDetectorClient()
        res = client.detect_jailbreak_attempt()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AdversarialPromptJailbreakDetectorClient()
        print(json.dumps(client.detect_jailbreak_attempt(), indent=2))
