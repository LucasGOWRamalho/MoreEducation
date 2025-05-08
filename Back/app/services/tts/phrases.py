import json
import os
from typing import Dict, List

class PhraseManager:
    def __init__(self, phrases_file: str = "phrases.json"):
        self.phrases_file = phrases_file
        self.phrases = self._load_phrases()
        
    def _load_phrases(self) -> Dict[str, List[str]]:
        """Carrega frases pré-definidas"""
        default_phrases = {
            "cumprimentos": ["Olá", "Bom dia", "Por favor"],
            "necessidades": ["Água", "Comida", "Banheiro"],
            "emergencia": ["Ajuda", "Médico", "Urgência"]
        }
        
        try:
            if os.path.exists(self.phrases_file):
                with open(self.phrases_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return default_phrases
        except Exception:
            return default_phrases
            
    def get_category(self, category: str) -> List[str]:
        """Obtém frases de uma categoria"""
        return self.phrases.get(category, [])
        
    def add_phrase(self, category: str, phrase: str):
        """Adiciona nova frase"""
        if category not in self.phrases:
            self.phrases[category] = []
        self.phrases[category].append(phrase)
        self._save_phrases()
        
    def _save_phrases(self):
        """Salva frases no arquivo"""
        with open(self.phrases_file, 'w', encoding='utf-8') as f:
            json.dump(self.phrases, f, ensure_ascii=False, indent=2)