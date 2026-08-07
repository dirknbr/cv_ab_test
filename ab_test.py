
from google import genai
from google.genai import types
import pandas as pd

api_key = 'xxx'
client = genai.Client(api_key=api_key)

# upload the files to the Gemini API
cv1_file = client.files.upload(file="cv1.txt")
cv2_file = client.files.upload(file="cv2.txt")
job_spec_file = client.files.upload(file="jobspec.txt")

prompt = """
Your task is to compare 2 CVs and decide which one is more relevant for the job spec.

Give a detailed explanation why one CV is better than the other.

Use these criteria
- relevant experience
- number of years of experience
- technical and soft skills
- is the candidate too junior or senior

If there is a tie on some criteria make that clear as well.

You can make things more quantitative, eg CV1 is better in 3 categories, while CV2 is better in 2.

"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        prompt,
        "********* Job spec:", job_spec_file,
        "********* CV1:", cv1_file,
        "********* CV2:", cv2_file
    ])

print(response.text)