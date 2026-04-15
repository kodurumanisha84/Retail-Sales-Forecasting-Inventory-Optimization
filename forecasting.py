def train_model(df):
    X = df[['day','month','weekday','product_code']]
    y = df['sales']
    
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model

def predict(model, df):
    X = df[['day','month','weekday','product_code']]
    df['predicted_sales'] = model.predict(X)
    return df