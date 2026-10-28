import json
import os


class CareerEngineV2:
    def __init__(self, json_path="data/regras_carreiras.json"):
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Base de conhecimento não encontrada em: {json_path}")

        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.dimensoes = self.data["dimensoes"]
        self.trilhas = self.data["trilhas"]

    def calcular_compatibilidade(self, respostas_usuario):
        """
        Calcula a aderência do perfil do usuário para cada trilha usando a distância
        absoluta entre a resposta do usuário (1 a 5) e o peso ideal da trilha.
        """
        resultados = []
        max_diff_por_pergunta = 4
        total_perguntas = len(self.dimensoes)
        max_diff_total = max_diff_por_pergunta * total_perguntas

        for id_trilha, info in self.trilhas.items():
            pesos_ideais = info["pesos_ideais"]
            soma_diff = 0

            for dim in self.dimensoes:
                dim_id = dim["id"]
                nota_usuario = respostas_usuario.get(dim_id, 3)
                nota_ideal = pesos_ideais.get(dim_id, 3)

                soma_diff += abs(nota_usuario - nota_ideal)

            compatibilidade = 100 - ((soma_diff / max_diff_total) * 100)

            resultados.append({
                "id": id_trilha,
                "nome": info["nome"],
                "compatibilidade": round(compatibilidade, 2),
                "roadmap": info["roadmap"],
                "pesos_ideais": pesos_ideais
            })

        resultados_ordenados = sorted(resultados, key=lambda x: x["compatibilidade"], reverse=True)
        return resultados_ordenados[:3]