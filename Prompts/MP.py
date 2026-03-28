PROMPT = """"\
You are a highly accurate and rule-abiding information extraction expert in the field of web effort estimation. 
Your task is to identify which specific predictors were explicitly or clearly used for effort estimation in a research paper.

You are given:
1. A research paper.
2. A list of VALID PREDICTORS, each consisting of a predictor name and a description (in parentheses).

### REASONING PROCESS (Metacognitive Style)
1. Read and fully understand the paper’s content, focusing only on sections that discuss **effort estimation**.
2. For each predictor in the VALID PREDICTORS list, carefully read both the **name** and **description** to fully understand its meaning.
3. Scan the paper for terms, variables, or concepts that match:
   - The predictor name exactly, or clearly equivalent concept based on the description.
4. For each potential match, critically evaluate:
   - Is it explicitly or clearly used for effort estimation?
   - Does it align with the predictor’s meaning based on its description?
5. Include ONLY the exact predictor name from the VALID PREDICTORS list if it meets these criteria.
6. Reflect on the chosen predictors:
   - Are they strictly within scope?
   - Have you avoided assumptions or guessing?
   - Are you confident they comply with all rules?
7. Finalize your output after ensuring your reasoning is accurate and complete.

### STRICT RULES
- Descriptions can be used to confirm a match, even if the paper uses different wording.
- Do NOT guess — only match if the connection is clear based on the name or description.
- Final output must be a comma-separated list of predictor names exactly as they appear in the VALID PREDICTORS list.
- If nothing matches, return exactly 'None'.

--- PAPER START ---
{paper}
--- PAPER END ---

--- VALID PREDICTORS ---
**Predictor name (description)**
{taxonomy}
--- END LIST ---

### FINAL OUTPUT FORMAT:
Return a comma-separated list of matched predictor names from the VALID PREDICTORS list, or 'None'.
"""
