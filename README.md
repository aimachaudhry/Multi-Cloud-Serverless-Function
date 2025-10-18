# Multi-Cloud-Serverless-Function

In this assignment, a HTTP serverless function was deployed in **Google Cloud** and **Microsoft Azure** to classify a laboratory value: **serum cholesterol**

Each function accepts an input which is the cholesterol level and returns the output as either  *normal*  or *abnormal*, based on clinical thresholds.

The rule implemented was:

- **Normal**: cholesterol < 200 mg/dL

- **Abnormal**: cholesterol ≥ 200 mg/dL

Citation: Cleveland Clinic. *Cholesterol Numbers: What Do They Mean?* https://my.clevelandclinic.org/health/articles/11920-cholesterol-numbers-what-do-they-mean

## Zoom Recording:
https://drive.google.com/file/d/1YqsKowuWDc7phetHcVEJc0N1NDAYVQ1v/view?usp=sharing

## Google Cloud Provider (GCP)
### Steps:
1. Write a function in the Cloud Run interface
2. Choose **Inline editor** to the code directly
3. Select the Region
4. Set the Runtime to **Python 3.13**
5. Set Authentication to **Allow public access**
6. Choose **Request-based** for billing
7. Set **Minimum instances** to 1
8. Select Ingress: **Allow all traffic**
9. Click **Create** and save and deploy your function
10. Get the Function URL from the GCP Console and use it to test GET or POST requests

### Endpoint URL:
https://python-cholesterol-504-65399689449.europe-west1.run.app

<img width="880" height="327" alt="Screenshot 2025-10-17 at 6 35 39 PM" src="https://github.com/user-attachments/assets/2dc97580-9b6e-4ef7-9db2-cc669375f800" />



### Testing:



<img width="1142" height="502" alt="Screenshot 2025-10-17 at 6 44 59 PM" src="https://github.com/user-attachments/assets/631cdd83-47c1-46e9-8204-fa59ce5f5f23" />

## Azure
### Steps:
1. Create a **Function App**
2. Choose **Consumption Plan**
3. Choose **Python** as the Runtime (this will automatically choose **Linux**
4. **Review** and **Create** the Function App
5. Create a Function within the Function App:
   - **Template**: HTTP trigger
   - **Authorization level**: Function (requires a key).
6. Add your code and save and deploy your function
7. Get the Function URL to test requests

### Endpoint URL:

https://python-test-dev1-dfhphcddb0byhzc0.canadacentral-01.azurewebsites.net/api/cholesterol

<img width="1122" height="263" alt="Screenshot 2025-10-17 at 7 52 01 PM" src="https://github.com/user-attachments/assets/c2e0f4fe-2f0a-4638-ab41-3ffc2e199262" />



### Testing:

<img width="1288" height="621" alt="Screenshot 2025-10-17 at 8 33 56 PM" src="https://github.com/user-attachments/assets/af1add1c-88a3-4e66-994b-9fd6f220de03" />


## Comparison of GCP & Azure
Deploying the serverless function on GCP felt more streamlined and easier to test. This is because it was easier to access a public URL for testing. On the other hand, Azure offered more triggers and had a function key for the HTTP requests, which added complexity. However, Azure did have a built-in test interface, which made it convenient to run and debug functions.
