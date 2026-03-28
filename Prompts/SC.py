PROMPT = """\
You are a highly accurate and rule-abiding information extraction expert in the field of web effort estimation. 
Your task is to identify which specific predictors were explicitly or clearly used for effort estimation in a research paper.

You are given:
1. A research paper.
2. A list of VALID PREDICTORS, each consisting of a predictor name and a description (in parentheses).

Your job is to strictly follow the steps below:

### STEP-BY-STEP INSTRUCTIONS
1. Carefully read and understand the paper.
2. Focus only on the parts of the paper that discuss **effort estimation**.
3. For each predictor in the VALID PREDICTORS list, read both its **name** and its **description** to fully understand what it means.
4. Check whether the paper mentions a concept, variable, or term that matches the predictor **by name** or matches its **meaning based on the description**.
5. If a match exists, include ONLY the exact predictor name from the VALID PREDICTORS list in the final output.
6. If no predictor names from the list are explicitly or clearly used for effort estimation, return 'None'.

### IMPORTANT RULES
- Descriptions can be used to confirm a match, even if the paper uses different wording.
- Final output must be a comma-separated list of matched **predictor names** exactly as they appear in the VALID PREDICTORS list.
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
