#!/usr/bin/env python3
"""
새로운 카드 hBP03-045 기능 테스트
"""

import json
import sys
import os

# app 디렉토리를 Python 경로에 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.card_database import CardDatabase
from app.gameengine import GameEngine, Condition

def test_new_card():
    """새로운 카드가 정상적으로 로드되는지 테스트"""
    print("=== 새로운 카드 hBP03-045 테스트 ===")
    
    # 카드 데이터베이스 로드
    card_db = CardDatabase()
    
    # 새로운 카드가 존재하는지 확인
    card = card_db.get_card_by_id("hBP03-045")
    if card:
        print("✅ 카드 hBP03-045가 성공적으로 로드되었습니다.")
        print(f"   이름: {card['card_names']}")
        print(f"   타입: {card['card_type']}")
        print(f"   색상: {card['colors']}")
        print(f"   HP: {card['hp']}")
        print(f"   Buzz: {card.get('buzz', False)}")
        print(f"   Down Life Cost: {card.get('down_life_cost', 0)}")
        
        # 아츠 확인
        if 'arts' in card and len(card['arts']) > 0:
            art = card['arts'][0]
            print(f"   아츠: {art['art_id']}")
            print(f"   파워: {art['power']}")
            if 'art_effects' in art and len(art['art_effects']) > 0:
                effect = art['art_effects'][0]
                print(f"   아츠 효과: {effect['effect_type']}")
                print(f"   amount_per: {effect.get('amount_per', 'N/A')}")
                print(f"   per: {effect.get('per', 'N/A')}")
        
        # 브룸 이펙트 확인
        if 'bloom_effects' in card and len(card['bloom_effects']) > 0:
            bloom_effect = card['bloom_effects'][0]
            print(f"   브룸 이펙트: {bloom_effect['effect_type']}")
            if 'choice' in bloom_effect and len(bloom_effect['choice']) > 0:
                choice = bloom_effect['choice'][0]
                if 'and' in choice and len(choice['and']) > 0:
                    damage_effect = choice['and'][0]
                    print(f"   대미지 효과: {damage_effect['effect_type']}")
                    print(f"   multiple_targets: {damage_effect.get('multiple_targets', 'N/A')}")
                    print(f"   repeat: {damage_effect.get('repeat', 'N/A')}")
        
        return True
    else:
        print("❌ 카드 hBP03-045를 찾을 수 없습니다.")
        return False

def test_condition():
    """새로운 조건이 정상적으로 정의되어 있는지 테스트"""
    print("\n=== 새로운 조건 테스트 ===")
    
    # 조건이 정의되어 있는지 확인
    if hasattr(Condition, 'Condition_OpponentBackstageHpReducedCount'):
        print("✅ 새로운 조건이 정상적으로 정의되었습니다.")
        print(f"   조건: {Condition.Condition_OpponentBackstageHpReducedCount}")
        return True
    else:
        print("❌ 새로운 조건이 정의되지 않았습니다.")
        return False

def test_effect_type():
    """새로운 효과 타입이 정상적으로 정의되어 있는지 테스트"""
    print("\n=== 새로운 효과 타입 테스트 ===")
    
    from app.gameengine import EffectType
    
    # 효과 타입이 정의되어 있는지 확인
    if hasattr(EffectType, 'EffectType_PowerBoostPerCondition'):
        print("✅ 새로운 효과 타입이 정상적으로 정의되었습니다.")
        print(f"   효과 타입: {EffectType.EffectType_PowerBoostPerCondition}")
        return True
    else:
        print("❌ 새로운 효과 타입이 정의되지 않았습니다.")
        return False

def main():
    """메인 테스트 함수"""
    print("새로운 카드 hBP03-045 구현 테스트를 시작합니다...\n")
    
    results = []
    
    # 각 테스트 실행
    results.append(test_new_card())
    results.append(test_condition())
    results.append(test_effect_type())
    
    # 결과 요약
    print("\n=== 테스트 결과 요약 ===")
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ 모든 테스트가 통과했습니다! ({passed}/{total})")
        print("새로운 카드 hBP03-045가 성공적으로 구현되었습니다.")
    else:
        print(f"❌ 일부 테스트가 실패했습니다. ({passed}/{total})")
        print("구현을 다시 확인해주세요.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 