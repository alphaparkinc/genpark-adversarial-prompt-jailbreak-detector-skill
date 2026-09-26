import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AdversarialPromptJailbreakDetectorClient

def main():
    client = AdversarialPromptJailbreakDetectorClient()
    res = client.detect_jailbreak_attempt()
    print("=== Adversarial Prompt Jailbreak Detector Output ===")
    print(f"Jailbreak Detected: {res['jailbreak_detected']} (Risk Score: {res['jailbreak_risk_score']})")
    print(f"Safety Verdict: {res['safety_verdict']} | Action: {res['recommended_defense_action']}")
    print("\nAttack Vectors Identified:")
    for v in res['attack_vectors_identified']:
        print(f"  * [{v['attack_vector']}] weight={v['risk_weight']}")

if __name__ == '__main__':
    main()
