"""
Uniwersalny Żołnierz - Silnik bota e-commerce v3.0
Prototyp dla branży motoryzacyjnej z inteligentnym wyszukiwaniem i fuzzy matching
"""
import json
import os
from flask import session
from datetime import datetime
import random
import re
import requests
import uuid
import hashlib
import time
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz, process


class EcommerceBot:
    def __init__(self):
        self.product_database = {}
        self.faq_database = {}
        self.orders_database = {}
        self.current_context = None
        self.initialize_data()
    
    def initialize_data(self):
        """Inicjalizuje bazę danych dla branży motoryzacyjnej"""
        
        # Baza produktów motoryzacyjnych
        self.product_database = {
            'products': [
    # KLOCKI HAMULCOWE - rozszerzone
    {'id': 'KH001', 'name': 'Klocki hamulcowe przód Bosch BMW E90 320i', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'Bosch', 'model': '0986494104', 'price': 189.00, 'stock': 45},
    {'id': 'KH002', 'name': 'Klocki hamulcowe tył ATE Mercedes W204 C200', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'ATE', 'model': '13.0460-7218', 'price': 156.00, 'stock': 38},
    {'id': 'KH003', 'name': 'Klocki hamulcowe Ferodo Audi A4 B8 2.0 TDI', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'Ferodo', 'model': 'FDB4050', 'price': 245.00, 'stock': 22},
    {'id': 'KH004', 'name': 'Klocki hamulcowe TRW VW Golf VII 1.4 TSI', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'TRW', 'model': 'GDB1748', 'price': 135.00, 'stock': 67},
    {'id': 'KH005', 'name': 'Klocki hamulcowe Brembo Toyota Corolla E12', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'Brembo', 'model': 'P83052', 'price': 156.00, 'stock': 73},
    
    # TARCZE HAMULCOWE - rozszerzone
    {'id': 'TH001', 'name': 'Tarcza hamulcowa przednia Brembo BMW E90 320mm', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'Brembo', 'model': '09.9772.11', 'price': 420.00, 'stock': 18},
    {'id': 'TH002', 'name': 'Tarcza hamulcowa tylna ATE Mercedes W204 300mm', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'ATE', 'model': '24.0330-0184', 'price': 285.00, 'stock': 25},
    {'id': 'TH003', 'name': 'Tarcza hamulcowa Zimmermann VW Golf VII przód 312mm', 'category': 'hamulce', 'machine': 'osobowy', 'brand': 'Zimmermann', 'model': '100.3234.20', 'price': 198.00, 'stock': 34},
    
    # FILTRY - znacznie rozszerzone
    {'id': 'FO001', 'name': 'Filtr oleju Mann HU719/7x BMW N47 N57 diesel', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Mann', 'model': 'HU719/7x', 'price': 62.00, 'stock': 120},
    {'id': 'FO002', 'name': 'Filtr oleju Mahle OX371D Mercedes OM651 2.2 CDI', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Mahle', 'model': 'OX371D', 'price': 45.00, 'stock': 89},
    {'id': 'FO003', 'name': 'Filtr oleju Bosch F026407022 VW 1.9 2.0 TDI', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Bosch', 'model': 'F026407022', 'price': 38.00, 'stock': 156},
    {'id': 'FO004', 'name': 'Filtr oleju UFI 25.106.00 Fiat Multijet 1.3 1.9', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'UFI', 'model': '25.106.00', 'price': 28.00, 'stock': 134},
    
    {'id': 'FP001', 'name': 'Filtr paliwa Bosch F026402836 PSA 1.6 2.0 HDI', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Bosch', 'model': 'F026402836', 'price': 89.00, 'stock': 85},
    {'id': 'FP002', 'name': 'Filtr paliwa Mann WK853/3x Mercedes Sprinter 2.2', 'category': 'filtry', 'machine': 'dostawczy', 'brand': 'Mann', 'model': 'WK853/3x', 'price': 67.00, 'stock': 76},
    {'id': 'FP003', 'name': 'Filtr paliwa Mahle KL440/18 BMW 118d 120d 320d', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Mahle', 'model': 'KL440/18', 'price': 78.00, 'stock': 93},
    
    {'id': 'FA001', 'name': 'Filtr powietrza K&N 33-2990 sportowy uniwersalny', 'category': 'filtry', 'machine': 'uniwersalny', 'brand': 'K&N', 'model': '33-2990', 'price': 285.00, 'stock': 35},
    {'id': 'FA002', 'name': 'Filtr powietrza Mann C2774/1 BMW E90 E91 E92', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Mann', 'model': 'C2774/1', 'price': 67.00, 'stock': 89},
    {'id': 'FA003', 'name': 'Filtr powietrza Bosch F026400200 VW Golf V VI VII', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Bosch', 'model': 'F026400200', 'price': 54.00, 'stock': 112},
    
    {'id': 'FK001', 'name': 'Filtr kabinowy węglowy Mann CUK2939 Audi A4 A6', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Mann', 'model': 'CUK2939', 'price': 95.00, 'stock': 68},
    {'id': 'FK002', 'name': 'Filtr kabinowy Bosch 1987432436 BMW E90 E91 E92', 'category': 'filtry', 'machine': 'osobowy', 'brand': 'Bosch', 'model': '1987432436', 'price': 78.00, 'stock': 84},
    
    # AMORTYZATORY - więcej marek
    {'id': 'AM001', 'name': 'Amortyzator przód Bilstein B4 VW Golf VII 1.4 TSI', 'category': 'zawieszenie', 'machine': 'osobowy', 'brand': 'Bilstein', 'model': '22-266767', 'price': 520.00, 'stock': 15},
    {'id': 'AM002', 'name': 'Amortyzator tył KYB Excel-G Ford Focus MK3 1.6', 'category': 'zawieszenie', 'machine': 'osobowy', 'brand': 'KYB', 'model': '349034', 'price': 385.00, 'stock': 24},
    {'id': 'AM003', 'name': 'Amortyzator przód Sachs Opel Astra J 1.7 CDTI', 'category': 'zawieszenie', 'machine': 'osobowy', 'brand': 'Sachs', 'model': '314896', 'price': 425.00, 'stock': 19},
    {'id': 'AM004', 'name': 'Amortyzator Monroe BMW E90 320d przód', 'category': 'zawieszenie', 'machine': 'osobowy', 'brand': 'Monroe', 'model': 'G7411', 'price': 398.00, 'stock': 28},
    
    # ŚWIECE ZAPŁONOWE I ŻAROWE - rozszerzone
    {'id': 'SZ001', 'name': 'Świeca zapłonowa NGK Laser Iridium ILZKR7B11', 'category': 'zapłon', 'machine': 'osobowy', 'brand': 'NGK', 'model': 'ILZKR7B11', 'price': 45.00, 'stock': 280},
    {'id': 'SZ002', 'name': 'Świeca zapłonowa Bosch Platinum Plus FR7DPP33', 'category': 'zapłon', 'machine': 'osobowy', 'brand': 'Bosch', 'model': 'FR7DPP33', 'price': 38.00, 'stock': 320},
    {'id': 'SZ003', 'name': 'Świeca żarowa Beru PSG006 Mercedes 2.2 CDI', 'category': 'zapłon', 'machine': 'osobowy', 'brand': 'Beru', 'model': 'PSG006', 'price': 78.00, 'stock': 145},
    {'id': 'SZ004', 'name': 'Świeca zapłonowa Champion RC89YCC BMW N52 N54', 'category': 'zapłon', 'machine': 'osobowy', 'brand': 'Champion', 'model': 'RC89YCC', 'price': 42.00, 'stock': 167},
    {'id': 'SZ005', 'name': 'Świeca zapłonowa Denso IK20TT VW Golf TSI TFSI', 'category': 'zapłon', 'machine': 'osobowy', 'brand': 'Denso', 'model': 'IK20TT', 'price': 51.00, 'stock': 234},
    
    # AKUMULATORY - więcej marek
    {'id': 'AK001', 'name': 'Akumulator Varta Blue Dynamic 74Ah 680A E12', 'category': 'elektryka', 'machine': 'osobowy', 'brand': 'Varta', 'model': 'E12', 'price': 420.00, 'stock': 38},
    {'id': 'AK002', 'name': 'Akumulator Bosch S4 Silver 60Ah 540A S4005', 'category': 'elektryka', 'machine': 'osobowy', 'brand': 'Bosch', 'model': 'S4005', 'price': 350.00, 'stock': 45},
    {'id': 'AK003', 'name': 'Akumulator Exide Premium 77Ah 760A EA770', 'category': 'elektryka', 'machine': 'osobowy', 'brand': 'Exide', 'model': 'EA770', 'price': 389.00, 'stock': 32},
    {'id': 'AK004', 'name': 'Akumulator Yuasa YBX5027 62Ah 540A Silver', 'category': 'elektryka', 'machine': 'osobowy', 'brand': 'Yuasa', 'model': 'YBX5027', 'price': 356.00, 'stock': 29},
    
    # OLEJE SILNIKOWE - więcej marek
    {'id': 'OL001', 'name': 'Olej silnikowy Castrol Edge 5W30 Titanium FST 5L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Castrol', 'model': 'Edge 5W30', 'price': 165.00, 'stock': 92},
    {'id': 'OL002', 'name': 'Olej silnikowy Mobil 1 ESP 0W40 syntetyczny 4L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Mobil', 'model': 'ESP 0W40', 'price': 189.00, 'stock': 78},
    {'id': 'OL003', 'name': 'Olej silnikowy Shell Helix Ultra 5W40 API SN 5L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Shell', 'model': 'Helix Ultra', 'price': 145.00, 'stock': 110},
    {'id': 'OL004', 'name': 'Olej silnikowy Total Quartz 9000 5W40 ACEA C3 5L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Total', 'model': 'Quartz 9000', 'price': 156.00, 'stock': 87},
    {'id': 'OL005', 'name': 'Olej silnikowy Motul 8100 X-cess 5W40 VW 502.00 5L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Motul', 'model': '8100 X-cess', 'price': 198.00, 'stock': 54},
    {'id': 'OL006', 'name': 'Olej silnikowy Liqui Moly Top Tec 4200 5W30 5L', 'category': 'oleje', 'machine': 'osobowy', 'brand': 'Liqui Moly', 'model': 'Top Tec 4200', 'price': 234.00, 'stock': 43}
],
            'categories': {
                'hamulce': '🔧 Układ hamulcowy',
                'filtry': '🔍 Filtry',
                'zawieszenie': '🚗 Zawieszenie',
                'zapłon': '⚡ Układ zapłonowy',
                'elektryka': '🔋 Elektryka',
                'oleje': '🛢️ Oleje i płyny'
            },
            'machines': {
                'osobowy': '🚗 Samochód osobowy',
                'dostawczy': '🚐 Samochód dostawczy',
                'ciężarowy': '🚚 Samochód ciężarowy',
                'motocykl': '🏍️ Motocykl',
                'uniwersalny': '🔧 Uniwersalne'
            }
        }
        
        # FAQ dla branży motoryzacyjnej
        self.faq_database = [
            {
                'id': 'FAQ001',
                'keywords': ['dostawa', 'wysyłka', 'kiedy', 'czas dostawy', 'przesyłka', 'kurier', 'odbiór'],
                'question': 'Jaki jest czas dostawy części samochodowych?',
                'answer': '🚚 **Opcje dostawy:**\n\n• **Dostawa kurierem:** 24h dla produktów na stanie\n• **Odbiór osobisty:** tego samego dnia do godz. 18:00\n• **Dostawa ekspresowa:** do 4h w wybranych miastach (+49 zł)\n• **Części na zamówienie:** 2-5 dni roboczych\n\n✅ Darmowa dostawa od 299 zł!',
                'category': 'dostawa'
            },
            {
                'id': 'FAQ002',
                'keywords': ['zwrot', 'reklamacja', 'wymiana', 'gwarancja', 'wadliwa część'],
                'question': 'Jak zwrócić lub wymienić część?',
                'answer': '↩️ **Zwroty i reklamacje:**\n\n• **14 dni** na zwrot bez montażu\n• **24 miesiące** gwarancji na wszystkie części\n• **Darmowa wymiana** przy wadzie fabrycznej\n• **Zwrot kosztów montażu** przy wadliwej części\n\n📝 Wypełnij formularz online i otrzymasz etykietę zwrotową',
                'category': 'zwroty'
            },
            {
                'id': 'FAQ003',
                'keywords': ['montaż', 'warsztat', 'mechanik', 'instalacja', 'wymiana'],
                'question': 'Czy oferujecie montaż części?',
                'answer': '🔧 **Usługi montażu:**\n\n• **Sieć 200+ warsztatów partnerskich** w całej Polsce\n• **Rabat 15%** na montaż przy zakupie u nas\n• **Gwarancja na montaż:** 12 miesięcy\n• **Umów montaż online** przy składaniu zamówienia\n\n📞 Pomoc w doborze warsztatu: 800-MONTAZ',
                'category': 'montaż'
            },
            {
                'id': 'FAQ004',
                'keywords': ['pasuje', 'kompatybilność', 'VIN', 'model', 'rocznik', 'dopasowanie'],
                'question': 'Jak sprawdzić czy część pasuje do mojego auta?',
                'answer': '🔍 **Sprawdzanie kompatybilności:**\n\n• **Wyszukiwarka po VIN** - 100% pewności\n• **Katalog TecDoc** - wybierz markę/model/rocznik\n• **Czat z ekspertem** - pomoc w doborze\n• **Numer OE części** - znajdziemy zamiennik\n\n💡 W razie wątpliwości wyślij nam zdjęcie tabliczki znamionowej',
                'category': 'dobór'
            }
        ]
        
        # Przykładowe zamówienia
        self.orders_database = {
            'MOT-2024001': {
                'status': '🚚 W drodze',
                'details': 'Przesyłka nadana dziś o 14:30. Dostawa jutro do 12:00',
                'tracking': 'DPD: 0123456789',
                'items': ['Klocki hamulcowe Bosch BMW E90', 'Filtr oleju Mann HU719/7x']
            },
            'MOT-2024002': {
                'status': '✅ Dostarczone',
                'details': 'Dostarczone wczoraj o 16:45. Podpis: J.Kowalski',
                'tracking': 'InPost: 670000123456',
                'items': ['Amortyzator Bilstein B4 (2 szt.)', 'Olej Castrol Edge 5W30']
            }
        }

    def send_ga4_no_results_event(self, query, search_type='products'):
        """
        Send 'search_no_results' event to Google Analytics 4 via Measurement Protocol
        
        Args:
            query (str): Search query that returned no results
            search_type (str): Type of search ('products' or 'faq')
        
        Returns:
            bool: True if successfully sent, False otherwise
        """
        try:
            # GA4 Measurement Protocol configuration
            # UWAGA: Podmień te wartości na swoje rzeczywiste
            GA4_MEASUREMENT_ID = "G-ECOMMERCE123"  # Podmień na swój Measurement ID
            GA4_API_SECRET = "YOUR_API_SECRET_HERE"  # Podmień na swój API Secret
            
            # Generate consistent client_id for session tracking
            # Można też użyć session ID z Flask
            session_data = f"universal_soldier_{int(time.time() // 3600)}"  # Per hour sessions
            client_id = hashlib.md5(session_data.encode()).hexdigest()
            
            # GA4 Measurement Protocol endpoint
            url = f"https://www.google-analytics.com/mp/collect"
            
            # Request parameters
            params = {
                'measurement_id': GA4_MEASUREMENT_ID,
                'api_secret': GA4_API_SECRET
            }
            
            # Event payload
            payload = {
                "client_id": client_id,
                "events": [{
                    "name": "search_no_results",
                    "params": {
                        "search_term": query[:100],  # Limit length for GA4
                        "search_type": search_type,
                        "source": "universal_soldier_bot",
                        "query_length": len(query),
                        "timestamp": int(time.time()),
                        "session_id": client_id[:16]
                    }
                }]
            }
            
            # Send POST request
            response = requests.post(
                url, 
                params=params, 
                json=payload, 
                timeout=5  # 5 second timeout
            )
            
            # Log success/failure
            if response.status_code == 204:  # GA4 returns 204 on success
                print(f"[GA4] ✅ No results event sent: '{query}' ({search_type})")
                return True
            else:
                print(f"[GA4] ❌ Failed to send event. Status: {response.status_code}")
                print(f"[GA4] Response: {response.text}")
                return False
                
        except requests.exceptions.Timeout:
            print(f"[GA4] ⏱️ Timeout sending no results event for: '{query}'")
            return False
        except requests.exceptions.RequestException as e:
            print(f"[GA4] 🚫 Network error sending event: {e}")
            return False
        except Exception as e:
            print(f"[GA4] 💥 Unexpected error sending event: {e}")
            import traceback
            traceback.print_exc()
            return False

    def normalize_query(self, query):
        """Normalizacja zapytania - obsługa literówek typowych dla motoryzacji"""
        query = query.lower().strip()
        
        # Korekta popularnych literówek w motoryzacji
        typo_corrections = {
            'kloki': 'klocki',
            'klocek': 'klocki',
            'hamulec': 'hamulce',
            'amortyztor': 'amortyzator',
            'amortyzaor': 'amortyzator',
            'filtr': 'filtr',
            'filetr': 'filtr',
            'swica': 'świeca',
            'swieca': 'świeca',
            'akumulator': 'akumulator',
            'akumlator': 'akumulator',
            'bateria': 'akumulator',
            'bosch': 'bosch',
            'bosh': 'bosch',
            'mann': 'mann',
            'man': 'mann',
            'brembo': 'brembo',
            'brebo': 'brembo'
        }
        
        for typo, correction in typo_corrections.items():
            query = query.replace(typo, correction)
        
        # Liczba mnoga/pojedyncza
        plural_singular = {
            'klocki': 'klocki',
            'klocków': 'klocki',
            'tarcze': 'tarcza',
            'tarcz': 'tarcza',
            'filtry': 'filtr',
            'filtrów': 'filtr',
            'świece': 'świeca',
            'świec': 'świeca',
            'amortyzatory': 'amortyzator',
            'amortyzatorów': 'amortyzator',
            'oleje': 'olej',
            'olejów': 'olej'
        }
        
        for plural, singular in plural_singular.items():
            query = query.replace(plural, singular)
        
        query = ' '.join(query.split())
        return query
    
    def get_fuzzy_product_matches(self, query, machine_filter=None, limit=6):
        """Inteligentne dopasowanie produktów z fuzzy matching i kontekstowym ważeniem"""
        query = self.normalize_query(query)
        matches = []
        
        # Wagi dla różnych typów dopasowań
        weights = {
    'exact_id': 100,
    'exact_name': 95,    # Zwiększ z 90
    'brand': 90,         # Zwiększ z 85
    'model': 88,         # Zwiększ z 80
    'category': 85,      # Zwiększ z 70
    'partial': 75,       # Zwiększ z 60
    'token': 65          # Zwiększ z 50
}
        
        for product in self.product_database['products']:
            if machine_filter and product['machine'] != machine_filter and product['machine'] != 'uniwersalny':
                continue
                
            # Inicjalizacja bazowego wyniku
            final_score = 0
            
            # 1. Sprawdzanie dokładnych dopasowań
            if query == product['id'].lower():
                final_score = weights['exact_id']
            elif query == product['name'].lower():
                final_score = weights['exact_name']
                
            # 2. Dopasowania marki i modelu
            brand_score = fuzz.ratio(query, product['brand'].lower())
            if brand_score > 85:
                final_score = max(final_score, weights['brand'])
                
            model_score = fuzz.ratio(query, product['model'].lower())
            if model_score > 85:
                final_score = max(final_score, weights['model'])
                
            # 3. Dopasowanie kategorii
            if query in product['category'].lower():
                final_score = max(final_score, weights['category'])
                
            # 4. Dopasowania częściowe i tokenowe
            if not final_score:  # Jeśli nie znaleziono dokładnych dopasowań
                search_text = f"{product['name']} {product['category']} {product['brand']} {product['model']}"
                search_text = search_text.lower()
                
                # Częściowe dopasowania
                partial_score = fuzz.partial_ratio(query, search_text)
                if partial_score > 75:
                    final_score = max(final_score, weights['partial'] * (partial_score / 100))
                
                # Dopasowania tokenów
                token_score = fuzz.token_set_ratio(query, search_text)
                if token_score > 60:
                    final_score = max(final_score, weights['token'] * (token_score / 100))
                    
                # Bonus za dopasowanie fragmentów
                query_words = query.split()
                product_words = search_text.split()
                for q_word in query_words:
                    if len(q_word) > 2:  # Ignorujemy krótkie słowa
                        for p_word in product_words:
                            if q_word in p_word and len(p_word) > 2:
                                final_score += 5  # Mały bonus za każde dopasowanie fragmentu
                
            # 5. Normalizacja końcowego wyniku
            final_score = min(100, final_score)
            
            # Dodaj do wyników jeśli przekroczono próg
            if final_score >= 35:
                matches.append((product, final_score))
        
        # Sortowanie po wyniku
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:limit]
    
    def get_fuzzy_faq_matches(self, query, limit=5):
        """Dopasowanie FAQ z inteligentnym ważeniem kontekstowym"""
        query = self.normalize_query(query)
        matches = []
        
        for faq in self.faq_database:
            # Przygotowanie tekstu do przeszukiwania
            question = faq['question'].lower()
            keywords = [k.lower() for k in faq['keywords']]
            category = faq.get('category', '').lower()
            
            # System punktacji
            final_score = 0
            
            # 1. Sprawdzanie dokładnych dopasowań
            if query == question:
                final_score = 100
            elif query in keywords:
                final_score = 90
                
            # 2. Dopasowania częściowe
            if not final_score:
                # Dopasowanie do pytania
                question_score = fuzz.ratio(query, question)
                if question_score > 80:
                    final_score = max(final_score, question_score)
                    
                # Dopasowanie do słów kluczowych
                for keyword in keywords:
                    keyword_score = fuzz.ratio(query, keyword)
                    if keyword_score > 85:
                        final_score = max(final_score, keyword_score + 5)
                
                # Dopasowanie tokenów
                search_text = f"{question} {' '.join(keywords)}"
                token_score = fuzz.token_set_ratio(query, search_text.lower())
                if token_score > 60:
                    final_score = max(final_score, token_score)
                    
                # Bonusy za dopasowania częściowe
                query_words = query.split()
                for q_word in query_words:
                    if len(q_word) > 2:  # Ignorujemy krótkie słowa
                        # Sprawdzamy w pytaniu
                        if q_word in question:
                            final_score += 5
                        # Sprawdzamy w słowach kluczowych
                        if any(q_word in k for k in keywords):
                            final_score += 8
                        # Bonus za dopasowanie kategorii
                        if category and q_word in category:
                            final_score += 10
                
            # Normalizacja wyniku
            final_score = min(100, final_score)
            
            # Dodawanie do wyników jeśli przekroczono próg
            if final_score >= 40:
                matches.append((faq, final_score))
                
        # Sortowanie po wyniku
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches[:limit]
    
    def search_products(self, query, machine_filter=None):
        """Wyszukiwanie produktów"""
        results = self.get_fuzzy_product_matches(query, machine_filter, limit=20)
        return [product for product, score in results]
    
    def search_faq(self, query):
        """Wyszukiwanie FAQ"""
        results = self.get_fuzzy_faq_matches(query, limit=10)
        return [faq for faq, score in results]
    
    def get_initial_greeting(self):
        """Powitanie dostosowane do branży motoryzacyjnej"""
        return {
            'text_message': """🚗 **Witaj w Auto Parts Pro**

Jestem Twoim ekspertem od części samochodowych. Pomogę Ci znaleźć idealną część lub odpowiem na pytania.

Co Cię interesuje?""",
            'buttons': [
                {'text': '🔧 Znajdź część', 'action': 'search_product'},
                {'text': '📦 Status zamówienia', 'action': 'order_status'},
                {'text': '❓ Mam pytanie', 'action': 'faq_search'},
                {'text': '🚚 Dostawa i koszty', 'action': 'faq_delivery'},
                {'text': '↩️ Zwroty i gwarancja', 'action': 'faq_returns'},
                {'text': '📞 Kontakt', 'action': 'contact'}
            ]
        }
    
    def handle_button_action(self, action):
        """Obsługa akcji przycisków"""
        session['context'] = action
        
        if action == 'search_product':
            return {
                'text_message': """🔧 **Wyszukiwarka części**

Wybierz typ pojazdu:""",
                'buttons': [
                    {'text': '🚗 Samochód osobowy', 'action': 'machine_osobowy'},
                    {'text': '🚐 Dostawczy', 'action': 'machine_dostawczy'},
                    {'text': '🏍️ Motocykl', 'action': 'machine_motocykl'},
                    {'text': '🔧 Części uniwersalne', 'action': 'machine_uniwersalny'},
                    {'text': '↩️ Powrót', 'action': 'main_menu'}
                ]
            }
        
        elif action.startswith('machine_'):
            machine_type = action.replace('machine_', '')
            session['machine_filter'] = machine_type
            
            machine_names = {
                'osobowy': 'Samochód osobowy',
                'dostawczy': 'Samochód dostawczy',
                'motocykl': 'Motocykl',
                'uniwersalny': 'Części uniwersalne'
            }
            
            return {
                'text_message': f"""✅ **{machine_names.get(machine_type, 'Pojazd')}**

Wpisz czego szukasz (nazwę części, markę, numer OE):""",
                'enable_input': True,
                'input_placeholder': 'np. klocki bosch, filtr mann, amortyzator...',
                'search_mode': True
            }
        
        elif action == 'faq_search':
            return {
                'text_message': """❓ **Centrum pomocy**

Wpisz swoje pytanie:""",
                'enable_input': True,
                'input_placeholder': 'np. jak sprawdzić czy część pasuje...',
                'faq_mode': True
            }
        
        elif action == 'order_status':
            return {
                'text_message': """📦 **Status zamówienia**

Wpisz numer (format: MOT-XXXXXXX):""",
                'enable_input': True,
                'input_placeholder': 'np. MOT-2024001'
            }
        
        elif action.startswith('faq_'):
            return self.handle_faq(action)
        
        elif action == 'contact':
            return {
                'text_message': """📞 **Kontakt**

**Infolinia:** 800 AUTO PARTS (bezpłatna)
**WhatsApp:** +48 500 100 200
**Email:** pomoc@autoparts.pl

⏰ Pon-Pt 8:00-20:00, Sob 9:00-16:00""",
                'buttons': [
                    {'text': '💬 Zadaj pytanie', 'action': 'faq_search'},
                    {'text': '↩️ Menu główne', 'action': 'main_menu'}
                ]
            }
        
        elif action == 'main_menu':
            return self.get_initial_greeting()
        
        elif action.startswith('add_to_cart_'):
            product_id = action.replace('add_to_cart_', '')
            return self.add_to_cart(product_id)
        
        elif action.startswith('product_details_'):
            product_id = action.replace('product_details_', '')
            return self.show_product_details(product_id)
        
        return {
            'text_message': 'Wybierz opcję:',
            'buttons': [{'text': '↩️ Menu główne', 'action': 'main_menu'}]
        }
    
    def handle_faq(self, action):
        """Obsługa FAQ"""
        faq_mapping = {
            'faq_delivery': 'FAQ001',
            'faq_returns': 'FAQ002'
        }
        
        faq_id = faq_mapping.get(action)
        if faq_id:
            faq = next((f for f in self.faq_database if f['id'] == faq_id), None)
            if faq:
                return {
                    'text_message': f"**{faq['question']}**\n\n{faq['answer']}",
                    'buttons': [
                        {'text': '❓ Inne pytanie', 'action': 'faq_search'},
                        {'text': '↩️ Menu główne', 'action': 'main_menu'}
                    ]
                }
        
        return {
            'text_message': 'Nie znaleziono odpowiedzi.',
            'buttons': [
                {'text': '📞 Kontakt', 'action': 'contact'},
                {'text': '↩️ Menu główne', 'action': 'main_menu'}
            ]
        }
    
    def process_message(self, message):
        """Przetwarzanie wiadomości"""
        context = session.get('context', '')
        
        if context == 'faq_search':
            faq_results = self.search_faq(message)
            
            if faq_results:
                best_match = faq_results[0]
                response = f"**{best_match['question']}**\n\n{best_match['answer']}"
                
                if len(faq_results) > 1:
                    response += "\n\n**Zobacz też:**"
                    for faq in faq_results[1:3]:
                        response += f"\n• {faq['question']}"
                
                return {
                    'text_message': response,
                    'buttons': [
                        {'text': '❓ Zadaj inne pytanie', 'action': 'faq_search'},
                        {'text': '↩️ Menu główne', 'action': 'main_menu'}
                    ]
                }
            else:
                return {
                    'text_message': """Nie znalazłem odpowiedzi.

📞 Zadzwoń: 800 AUTO PARTS
📧 Email: pomoc@autoparts.pl""",
                    'buttons': [
                        {'text': '❓ Spróbuj ponownie', 'action': 'faq_search'},
                        {'text': '↩️ Menu główne', 'action': 'main_menu'}
                    ]
                }
        
        elif context == 'order_status' or message.upper().startswith('MOT-'):
            order_num = message.upper()
            if order_num in self.orders_database:
                order = self.orders_database[order_num]
                items_list = '\n'.join([f"• {item}" for item in order['items']])
                
                return {
                    'text_message': f"""📦 **Zamówienie {order_num}**

**Status:** {order['status']}
**Szczegóły:** {order['details']}
**Tracking:** {order['tracking']}

**Produkty:**
{items_list}""",
                    'buttons': [
                        {'text': '📦 Sprawdź inne', 'action': 'order_status'},
                        {'text': '↩️ Menu główne', 'action': 'main_menu'}
                    ]
                }
            else:
                return {
                    'text_message': f"""❌ Nie znaleziono zamówienia {order_num}""",
                    'buttons': [
                        {'text': '🔄 Spróbuj ponownie', 'action': 'order_status'},
                        {'text': '↩️ Menu główne', 'action': 'main_menu'}
                    ]
                }
        
        elif session.get('machine_filter'):
            machine_filter = session.get('machine_filter')
            results = self.search_products(message, machine_filter)
            
            if not results:
                results = self.search_products(message)
                
                if results:
                    return {
                        'text_message': f"""⚠️ Nie znaleziono dla wybranego typu, ale mamy inne:

{self.format_product_results(results[:3])}""",
                        'buttons': self.create_product_buttons(results[:3])
                    }
                else:
                    return {
                        'text_message': """❌ Nie znaleziono produktów.

System automatycznie poprawia błędy. Spróbuj inaczej.""",
                        'buttons': [
                            {'text': '🔄 Szukaj ponownie', 'action': 'search_product'},
                            {'text': '↩️ Menu główne', 'action': 'main_menu'}
                        ]
                    }
            
            elif len(results) == 1:
                product = results[0]
                return self.show_product_details(product['id'])
            
            elif len(results) <= 5:
                return {
                    'text_message': f"""✅ Znaleziono {len(results)} produktów:

{self.format_product_results(results)}""",
                    'buttons': self.create_product_buttons(results)
                }
            
            else:
                return {
                    'text_message': f"""🔍 Znaleziono {len(results)} produktów. Top 5:

{self.format_product_results(results[:5])}""",
                    'buttons': self.create_product_buttons(results[:5])
                }
        
        return {
            'text_message': 'Wybierz opcję:',
            'buttons': [
                {'text': '🔧 Szukaj części', 'action': 'search_product'},
                {'text': '↩️ Menu główne', 'action': 'main_menu'}
            ]
        }
    
    def format_product_results(self, products):
        """Formatowanie wyników"""
        result = ""
        for product in products:
            stock_icon = "✅" if product['stock'] > 10 else "⚠️" if product['stock'] > 0 else "❌"
            result += f"""
**{product['name']}**
{product['id']} | {stock_icon} {product['stock']} szt. | {product['price']:.2f} zł
"""
        return result
    
    def create_product_buttons(self, products):
        """Przyciski produktów"""
        buttons = []
        for product in products[:4]:
            buttons.append({
                'text': f"🛒 {product['name'][:30]}... ({product['price']:.0f} zł)",
                'action': f"product_details_{product['id']}"
            })
        
        buttons.extend([
            {'text': '🔄 Szukaj ponownie', 'action': 'search_product'},
            {'text': '↩️ Menu główne', 'action': 'main_menu'}
        ])
        
        return buttons
    
    def show_product_details(self, product_id):
        """Szczegóły produktu"""
        product = None
        for p in self.product_database['products']:
            if p['id'] == product_id:
                product = p
                break
        
        if not product:
            return {
                'text_message': 'Produkt nie znaleziony.',
                'buttons': [{'text': '↩️ Menu główne', 'action': 'main_menu'}]
            }
        
        stock_status = "✅ Dostępny" if product['stock'] > 10 else "⚠️ Ostatnie sztuki" if product['stock'] > 0 else "❌ Na zamówienie"
        
        return {
            'text_message': f"""🔧 **{product['name']}**

📋 **Dane techniczne:**
• Kod: {product['id']}
• Producent: {product['brand']}
• Model: {product['model']}
• Kategoria: {self.product_database['categories'].get(product['category'], product['category'])}

💰 **Cena:** {product['price']:.2f} zł netto
💵 **Cena brutto:** {product['price'] * 1.23:.2f} zł

📦 **Dostępność:** {stock_status} ({product['stock']} szt.)
🚚 **Wysyłka:** 24h""",
            'buttons': [
                {'text': f"🛒 Dodaj do koszyka", 'action': f"add_to_cart_{product['id']}"},
                {'text': '🔍 Szukaj dalej', 'action': 'search_product'},
                {'text': '🏠 Menu główne', 'action': 'main_menu'}
            ]
        }
    
    def add_to_cart(self, product_id):
        """Dodanie do koszyka"""
        product = None
        for p in self.product_database['products']:
            if p['id'] == product_id:
                product = p
                break
        
        if not product:
            return {
                'text_message': 'Błąd dodawania do koszyka.',
                'buttons': [{'text': '↩️ Powrót', 'action': 'main_menu'}]
            }
        
        if 'cart' not in session:
            session['cart'] = []
        
        session['cart'].append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price']
        })
        session.modified = True
        
        cart_total = sum(item['price'] * 1.23 for item in session['cart'])
        
        return {
            'text_message': f"""✅ **Dodano do koszyka!**

🛒 {product['name']}
💰 {product['price'] * 1.23:.2f} zł brutto

**Koszyk ({len(session['cart'])} szt.):** {cart_total:.2f} zł

{'🎉 Darmowa dostawa!' if cart_total >= 299 else f'Do darmowej dostawy brakuje: {299 - cart_total:.2f} zł'}""",
            'cart_updated': True,
            'buttons': [
                {'text': '✅ Przejdź do kasy', 'action': 'checkout'},
                {'text': '🔍 Kontynuuj zakupy', 'action': 'search_product'},
                {'text': '↩️ Menu główne', 'action': 'main_menu'}
            ]
        }
    

def search_suggestions(self, query, context='products'):
    suggestions = []
    if context == 'faq':
        faq_results = self.get_fuzzy_faq_matches(query, limit=6)
        for faq, score in faq_results:
            suggestions.append({
                'title': faq['question'],
                'subtitle': f"Kategoria: {faq.get('category', 'FAQ')}",
                'icon': '❓',
                'score': int(score),
                'data': faq
            })
    else:
        product_results = self.get_fuzzy_product_matches(query, session.get('machine_filter'), limit=8)
        for product, score in product_results:
            suggestions.append({
                'title': product['name'],
                'subtitle': f"{product['brand']} • {product['price']:.0f} zł",
                'icon': '🔧',
                'score': int(score),
                'data': product
            })
    return suggestions
    