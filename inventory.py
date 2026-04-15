def inventory_optimization(df):
    avg_demand = df['predicted_sales'].mean()
    lead_time = 5
    
    safety_stock = avg_demand * 2
    reorder_point = (avg_demand * lead_time) + safety_stock
    
    result = df[['date','predicted_sales']].copy()
    result['reorder_point'] = reorder_point
    result['safety_stock'] = safety_stock
    
    return result