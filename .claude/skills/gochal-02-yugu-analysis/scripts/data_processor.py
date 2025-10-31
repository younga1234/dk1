#!/usr/bin/env python3
"""
유구 분석 데이터 처리 스크립트
다중 형식 입력 데이터를 표준 JSON으로 변환
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

def process_excel(filepath: str) -> Dict[str, Any]:
    """
    Excel/CSV 파일을 표준 JSON으로 변환
    
    Args:
        filepath: Excel/CSV 파일 경로
    
    Returns:
        표준 JSON 형식의 딕셔너리
    """
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas 라이브러리가 필요합니다. 'pip install pandas openpyxl' 실행", file=sys.stderr)
        sys.exit(1)
    
    # Excel 파일 읽기
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath, sheet_name='유구목록')
    
    # 유구 목록 변환
    yugu_list = []
    for _, row in df.iterrows():
        yugu = {
            "번호": str(row.get('번호', '')),
            "형태": str(row.get('형태', '')),
            "크기": str(row.get('크기', '')),
            "구성요소": str(row.get('구성요소', '')).split(',') if pd.notna(row.get('구성요소')) else [],
            "출토유물": str(row.get('출토유물', '')).split(',') if pd.notna(row.get('출토유물')) else []
        }
        yugu_list.append(yugu)
    
    return {
        "site_info": {
            "name": "유적명",
            "region": "지역",
            "period": "시대",
            "excavation_year": "발굴연도"
        },
        "data": {
            "유구목록": yugu_list
        }
    }

def process_markdown(text: str) -> Dict[str, Any]:
    """
    Markdown 텍스트를 표준 JSON으로 변환
    
    Args:
        text: Markdown 형식의 텍스트
    
    Returns:
        표준 JSON 형식의 딕셔너리
    """
    # 간단한 Markdown 파싱 (실제로는 더 복잡한 파서 필요)
    lines = text.split('\n')
    
    site_info = {}
    yugu_list = []
    current_yugu = None
    
    for line in lines:
        line = line.strip()
        
        # 유적 정보 파싱
        if line.startswith('- 유적명:'):
            site_info['name'] = line.replace('- 유적명:', '').strip()
        elif line.startswith('- 시대:'):
            site_info['period'] = line.replace('- 시대:', '').strip()
        elif line.startswith('- 지역:'):
            site_info['region'] = line.replace('- 지역:', '').strip()
        
        # 유구 정보 파싱
        elif line.startswith('### '):
            if current_yugu:
                yugu_list.append(current_yugu)
            current_yugu = {"번호": line.replace('### ', '').strip()}
        elif current_yugu and line.startswith('- 형태:'):
            current_yugu['형태'] = line.replace('- 형태:', '').strip()
        elif current_yugu and line.startswith('- 크기:'):
            current_yugu['크기'] = line.replace('- 크기:', '').strip()
        elif current_yugu and line.startswith('- 구성요소:'):
            components = line.replace('- 구성요소:', '').strip()
            current_yugu['구성요소'] = [c.strip() for c in components.split(',')]
        elif current_yugu and line.startswith('- 출토유물:'):
            artifacts = line.replace('- 출토유물:', '').strip()
            current_yugu['출토유물'] = [a.strip() for a in artifacts.split(',')]
    
    if current_yugu:
        yugu_list.append(current_yugu)
    
    return {
        "site_info": site_info,
        "data": {
            "유구목록": yugu_list
        }
    }

def process_json(filepath: str) -> Dict[str, Any]:
    """
    JSON 파일 로드
    
    Args:
        filepath: JSON 파일 경로
    
    Returns:
        JSON 데이터
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_data(data: Dict[str, Any]) -> bool:
    """
    데이터 유효성 검증
    
    Args:
        data: 검증할 데이터
    
    Returns:
        유효성 여부
    """
    required_fields = ['site_info', 'data']
    
    for field in required_fields:
        if field not in data:
            print(f"Error: 필수 필드 '{field}'가 없습니다.", file=sys.stderr)
            return False
    
    if '유구목록' not in data['data']:
        print("Error: '유구목록' 데이터가 없습니다.", file=sys.stderr)
        return False
    
    return True

def main():
    """메인 함수"""
    if len(sys.argv) < 2:
        print("Usage: python data_processor.py <input_file>")
        print("사용법: python data_processor.py <input_file>")
        print("지원 형식: .xlsx, .csv, .json, .md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    filepath = Path(input_file)
    
    if not filepath.exists():
        print(f"Error: 파일을 찾을 수 없습니다: {input_file}", file=sys.stderr)
        sys.exit(1)
    
    # 파일 형식에 따라 처리
    if filepath.suffix in ['.xlsx', '.xls', '.csv']:
        data = process_excel(str(filepath))
    elif filepath.suffix == '.json':
        data = process_json(str(filepath))
    elif filepath.suffix == '.md':
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        data = process_markdown(text)
    else:
        print(f"Error: 지원하지 않는 파일 형식입니다: {filepath.suffix}", file=sys.stderr)
        sys.exit(1)
    
    # 데이터 검증
    if not validate_data(data):
        sys.exit(1)
    
    # JSON 출력
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
