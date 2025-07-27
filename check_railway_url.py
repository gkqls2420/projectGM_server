#!/usr/bin/env python3
"""
Railway URL 확인 스크립트
Railway에서 배포된 서버의 URL을 확인하고 테스트합니다.
"""

import requests
import websocket
import json
import time
import sys

def check_railway_url(base_url):
    """Railway URL을 확인하고 테스트합니다."""
    print("=== Railway URL 확인 및 테스트 ===")
    print(f"기본 URL: {base_url}")
    print()
    
    # 1. HTTP 헬스체크
    print("1. HTTP 헬스체크 테스트...")
    try:
        health_url = f"{base_url}/health"
        response = requests.get(health_url, timeout=10)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ 헬스체크 성공: {health_data}")
        else:
            print(f"❌ 헬스체크 실패: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 헬스체크 오류: {e}")
        return False
    
    # 2. WebSocket 연결 테스트
    print("\n2. WebSocket 연결 테스트...")
    try:
        ws_url = base_url.replace("https://", "wss://").replace("http://", "ws://") + "/ws"
        print(f"WebSocket URL: {ws_url}")
        
        # WebSocket 연결 테스트
        ws = websocket.create_connection(ws_url, timeout=10)
        
        # 간단한 메시지 전송
        test_message = {
            "message_type": "join_server"
        }
        ws.send(json.dumps(test_message))
        
        # 응답 대기
        response = ws.recv()
        print(f"✅ WebSocket 연결 성공!")
        print(f"서버 응답: {response[:100]}...")  # 처음 100자만 표시
        
        ws.close()
        return True
        
    except Exception as e:
        print(f"❌ WebSocket 연결 실패: {e}")
        return False

def main():
    """메인 함수"""
    print("Railway URL 확인 도구")
    print("=" * 50)
    
    # 사용자로부터 URL 입력 받기
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = input("Railway 서비스 URL을 입력하세요 (예: https://your-app.railway.app): ").strip()
    
    if not base_url:
        print("URL이 입력되지 않았습니다.")
        return
    
    # URL 정규화
    if not base_url.startswith(("http://", "https://")):
        base_url = "https://" + base_url
    
    # 테스트 실행
    success = check_railway_url(base_url)
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 모든 테스트가 성공했습니다!")
        print("\n클라이언트 설정:")
        ws_url = base_url.replace("https://", "wss://").replace("http://", "ws://") + "/ws"
        print(f"WebSocket URL: {ws_url}")
        print("\nglobal_settings.gd에 다음을 설정하세요:")
        print(f'const railway_url = "{ws_url}"')
    else:
        print("❌ 일부 테스트가 실패했습니다.")
        print("Railway 서버가 정상적으로 배포되었는지 확인하세요.")

if __name__ == "__main__":
    main() 