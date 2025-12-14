import re
from collections import defaultdict

def analyze_log(file_path):
    """
    Analisa um arquivo de log para extrair estatísticas de acesso, erros e latência.
    """
    # Expressão Regular para extrair (Método, Rota, Status, Latência)
    # Exemplo de linha: 2025-12-13 10:00:06 GET /api/v1/reports/summary 500 1500ms
    # Padrão: (\w+)\s+([/\w]+)\s+(\d+)\s+(\d+)ms
    log_pattern = re.compile(r'\s(\w+)\s+([^ ]+)\s+(\d+)\s+(\d+)ms')
    
    # Dicionários para armazenar dados agregados
    endpoint_data = defaultdict(lambda: {'count': 0, 'errors': 0, 'total_latency': 0, 'latencies': []})
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                match = log_pattern.search(line)
                
                if match:
                    method, route, status_str, latency_str = match.groups()
                    key = f"{method} {route}"
                    status = int(status_str)
                    latency = int(latency_str)
                    
                    endpoint_data[key]['count'] += 1
                    endpoint_data[key]['total_latency'] += latency
                    endpoint_data[key]['latencies'].append(latency)
                    
                    # Checa por erros (4xx ou 5xx)
                    if status >= 400:
                        endpoint_data[key]['errors'] += 1
                        
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
        return

    # --- Processamento e Impressão de Resultados ---

    print("="*60)
    print("ANALISADOR DE LOGS - RELATÓRIO DE EFICIÊNCIA")
    print("="*60)
    
    # 1. Endpoints Mais Acessados (Top 3)
    print("\n--- 1. Endpoints Mais Acessados (Volume) ---")
    sorted_by_count = sorted(endpoint_data.items(), key=lambda item: item[1]['count'], reverse=True)
    
    for endpoint, data in sorted_by_count[:3]:
        print(f"[{data['count']} acessos] {endpoint}")

    # 2. Endpoints com Mais Erros (Status >= 400)
    print("\n--- 2. Endpoints com Problemas (Erros 4xx/5xx) ---")
    sorted_by_errors = sorted(endpoint_data.items(), key=lambda item: item[1]['errors'], reverse=True)
    
    for endpoint, data in sorted_by_errors:
        if data['errors'] > 0:
            print(f"[{data['errors']} erros] {endpoint} (Taxa de erro: {data['errors'] / data['count'] * 100:.1f}%)")

    # 3. Endpoints Mais Lentos (Latência Média)
    print("\n--- 3. Endpoints Lentos (Potenciais Gargalos) ---")
    
    # Calcula a latência média e ordena
    results_with_avg = []
    for endpoint, data in endpoint_data.items():
        avg_latency = data['total_latency'] / data['count']
        results_with_avg.append((endpoint, avg_latency))
        
    sorted_by_latency = sorted(results_with_avg, key=lambda item: item[1], reverse=True)
    
    for endpoint, avg_latency in sorted_by_latency:
        # Define um limite alto (ex: 500ms) para destacar gargalos
        marker = '⚠️' if avg_latency > 500 else ''
        print(f"{marker} Média: {avg_latency:.0f}ms - {endpoint}")


if __name__ == "__main__":
    # O arquivo deve estar no mesmo diretório
    analyze_log('server.log')