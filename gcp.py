import json
import functions_framework


@functions_framework.http
def cholesterol_classifier(request):
   cholesterol = request.args.get("cholesterol")
   if cholesterol is None:
       try:
           data = request.get_json(force=True, silent=True) or {}
       except Exception:
           data = {}
       cholesterol = data.get("cholesterol")

  # Presence check
   if cholesterol is None:
       return (
           json.dumps({"error": "Please provide ?cholesterol=VALUE in the URL or JSON body."}),
           400,
           {"Content-Type": "application/json"},
       )

    # Type/convert check
   try:
       chol_val = float(cholesterol)
   except (TypeError, ValueError):
       return (
           json.dumps({"error": "'cholesterol' must be a number."}),
           400,
           {"Content-Type": "application/json"},
       )

    # Classification logic
   if chol_val < 200:
       status = "normal"
       category = "Desirable (<200 mg/dL)"
   else:
       status = "abnormal"
       category = "High (≥200 mg/dL)"

    # Prepare payload
   payload = {
       "cholesterol": chol_val,
       "status": status,
       "category": category
   }

    # Return JSON response
   return json.dumps(payload), 200, {"Content-Type": "application/json"}
