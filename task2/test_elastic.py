import csv
import os
from elasticsearch import Elasticsearch, helpers
import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_company_score(es, index_name):
    if not es.indices.exists(index=index_name):
        print(f"Index {index_name} does not exist!")
        return 0  
    response = es.search(index=index_name, body={
        "query": {
            "match_all": {}
        },
        "_source": ["department_id", "score"],
        "size": 10000  
    })
    
    department_data = {}
    for hit in response['hits']['hits']:
        department_id = hit['_source']['department_id']
        score = hit['_source']['score']
        if department_id not in department_data:
            department_data[department_id] = []
        department_data[department_id].append(score)
    
    median_scores = [np.median(scores) for scores in department_data.values() if len(scores) > 0]
    
    if not median_scores:
        return 0  
    
    company_score = np.mean(median_scores)
    return min(90, max(0, company_score))

def save_to_elasticsearch(es, index_name, data):
    for department_id, department_data in data.items():
        for user_id, score in enumerate(department_data):
            es.index(index=index_name, body={
                'department_id': department_id,
                'user_id': user_id,
                'score': score
            })

def populate_index_from_csv(csv_file_path, es):
    index_name = os.path.basename(csv_file_path).replace('.csv', '')  
    actions = []
    
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            action = {
                "_op_type": "index",  
                "_index": index_name,
                "_source": {
                    "department_id": row['department_id'],
                    "user_id": int(row['user_id']),
                    "score": float(row['score']),
                }
            }
            actions.append(action)
    
    helpers.bulk(es, actions)

def populate_index_from_directory(directory_path, es):
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {csv_file_path}")
            populate_index_from_csv(csv_file_path, es)

def create_elasticsearch_client():
    es = Elasticsearch("http://localhost:9200", http_auth=("elastic", "elastic-search"))
    return es

if __name__ == "__main__":
    es = create_elasticsearch_client()
    
    csv_directory = "C:/Users/Tomi/Desktop/inf_428_hw_1/test_case_data"  
    
    populate_index_from_directory(csv_directory, es)
    print("Data from all CSV files populated into Elasticsearch indices.")
    
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            index_name = filename.replace('.csv', '')
            company_score = calculate_company_score(es, index_name)
            print(f"Company Score for {index_name}: {company_score}")

