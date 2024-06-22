def customer_churn_prediction():
    # User Inputs
    customer_id = input("Enter customer ID: ")
    age = int(input("Enter customer's age: "))
    usage_gb = int(input("Enter monthly data usage (in GB): "))
    
    # Custom churn prediction logic (dummy logic for example)
    if age > 50 and usage_gb > 100:
        churn_prediction = "High churn risk"
    else:
        churn_prediction = "Low churn risk"
    
    print(f"Customer ID: {customer_id}")
    print(f"Churn Prediction: {churn_prediction}")
    
customer_churn_prediction()