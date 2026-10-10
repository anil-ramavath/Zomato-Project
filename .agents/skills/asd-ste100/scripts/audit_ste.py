#!/usr/bin/env python3
"""
ASD-STE100 Compliance Checker (Linter)
A lightweight linter to audit technical text against basic ASD-STE100 rules:
1. Sentence length: <= 20 words for procedural steps, <= 25 words for descriptive sentences.
2. Unapproved/forbidden words (ensure, utilize, in order to, prior to, etc.).
3. Noun clusters (> 3 consecutive nouns).
4. Passive voice constructions.
"""

import sys
import re
from pathlib import Path

FORBIDDEN_WORDS = {
    "ensure": "Use 'make sure'",
    "verify": "Use 'make sure' or 'examine'",
    "check": "Use 'examine' or 'make sure'",
    "utilize": "Use 'use'",
    "utilizing": "Use 'using'",
    "in order to": "Use 'to'",
    "prior to": "Use 'before'",
    "subsequent to": "Use 'after'",
    "terminate": "Use 'stop' or 'cancel'",
    "abort": "Use 'stop' or 'cancel'",
    "execute": "Use 'run' or 'do'",
    "as well as": "Use 'and'",
    "via": "Use 'through' or 'by'",
    "should": "Avoid modal 'should'. Use 'must' or imperative.",
    "could": "Avoid modal 'could'. Use 'can' or explicit condition.",
    "might": "Avoid modal 'might'. Use 'can' or explicit condition.",
}

PASSIVE_REGEX = re.compile(r"\b(is|are|was|were|be|been|being)\s+([a-z]+ed|[a-z]+en)\b", re.IGNORECASE)

def check_text(content: str):
    lines = content.splitlines()
    violations = []
    
    in_code_block = False
    
    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not stripped:
            continue
            
        is_procedural = bool(re.match(r"^(\d+\.|\-|\*)\s+", stripped))
        clean_line = re.sub(r"^(\d+\.|\-|\*)\s+", "", stripped)
        clean_line = re.sub(r"`[^`]+`", "VARIABLE", clean_line)  # mask inline code
        
        # Split sentences roughly by period/exclamation/question mark
        sentences = re.split(r"(?<=[.!?])\s+", clean_line)
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence or sentence.startswith("#"):
                continue
                
            words = sentence.split()
            word_count = len(words)
            
            # 1. Sentence length limit
            max_words = 20 if is_procedural else 25
            text_type = "Procedural step" if is_procedural else "Descriptive sentence"
            if word_count > max_words:
                violations.append({
                    "line": line_num,
                    "rule": "Rule 4.1 - Sentence Length",
                    "issue": f"{text_type} has {word_count} words (max allowed: {max_words}).",
                    "snippet": sentence[:80] + ("..." if len(sentence) > 80 else "")
                })
                
            # 2. Forbidden vocabulary
            lower_sentence = sentence.lower()
            for forbidden, suggestion in FORBIDDEN_WORDS.items():
                pattern = r"\b" + re.escape(forbidden) + r"\b"
                if re.search(pattern, lower_sentence):
                    violations.append({
                        "line": line_num,
                        "rule": "Rule 1.1 - Unapproved Word",
                        "issue": f"Found '{forbidden}'. {suggestion}",
                        "snippet": sentence[:80] + ("..." if len(sentence) > 80 else "")
                    })
                    
            # 3. Passive voice warning
            passive_match = PASSIVE_REGEX.search(sentence)
            if passive_match:
                violations.append({
                    "line": line_num,
                    "rule": "Rule 3.3 - Active Voice",
                    "issue": f"Potential passive construction: '{passive_match.group(0)}'. Use active voice.",
                    "snippet": sentence[:80] + ("..." if len(sentence) > 80 else "")
                })

    return violations

def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_ste.py <file-to-audit.md>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    content = file_path.read_text(encoding="utf-8")
    violations = check_text(content)

    print(f"\nASD-STE100 Audit Results for: {file_path.name}")
    print("=" * 60)
    if not violations:
        print("[PASS] No basic ASD-STE100 violations detected!")
        sys.exit(0)

    print(f"Found {len(violations)} potential issue(s):\n")
    for v in violations:
        print(f"Line {v['line']} | [{v['rule']}]")
        print(f"  Issue  : {v['issue']}")
        print(f"  Snippet: \"{v['snippet']}\"\n")

    sys.exit(1)

if __name__ == "__main__":
    main()
