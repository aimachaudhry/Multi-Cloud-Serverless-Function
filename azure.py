import azure.functions as func
import json
import logging

# Create a FunctionApp with HTTP auth level set to 'Function'
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="cholesterol")
def cholesterol_func(req: func.HttpRequest) -> func.HttpResponse:
   logging.info("Processing cholesterol request.")

# Try to get 'cholesterol' from query parameters
   cholesterol = req.params.get("cholesterol")
   if not cholesterol:
       try:
           req_body = req.get_json()
           cholesterol = req_body.get("cholesterol")
       except:
           pass
         
  # If not found in query, try to get it from the JSON body
   if not cholesterol:
       return func.HttpResponse(json.dumps({"error": "Field 'cholesterol' is required."}), status_code=400)
   try:
       chol_val = float(cholesterol)
   except:
       return func.HttpResponse(json.dumps({"error": "'cholesterol' must be a number."}), status_code=400)
     
  # Classify cholesterol value
   if chol_val < 200:
       status = "normal"
       category = "Desirable (<200 mg/dL)"
   else:
       status = "abnormal"
       category = "High (≥200 mg/dL)"
     
   # Return JSON response with classification
   return func.HttpResponse(json.dumps({"cholesterol": chol_val, "status": status, "category": category}), status_code=200)
