import random
import time
from datetime import datetime

class EnglishLearningGame:
   def __init__(self, student_name):
      self.student_name = student_name
       # 헷갈리는 알파벳 그룹
      self.confused_letters = {
         'group1': ['b', 'd'],
         'group2': ['p', 'q'],
         'group3': ['l', 'r'],
         'group4': ['j', 'l'],
       }
      
   def letter_distinction_game(self, duration=60): # 1분 게임
        """헷갈리는 알파벳 구별 게임"""
        print("\n=== 알파벳 구별하기 게임 ===")
        print(f"안녕하세요 {self.student_name}! 알파벳 구별 게임을 시작할게요.")
        
        correct = 0
        total = 0
        
        start_time = time.time()
        while time.time() - start_time < duration:
            # 랜덤하게 그룹 선택
            group = random.choice(list(self.confused_letters.keys()))
            letters = self.confused_letters[group]
            correct_letter = random.choice(letters)
            
            print(f"\n이 알파벳을 따라 써보세요: {correct_letter}")
            answer = input("답을 입력하세요: ").lower()
            
            if answer == correct_letter:
                print("정답입니다! 👍")
                correct += 1
            else:
                print(f"아쉽네요. 정답은 {correct_letter}입니다.")
            total += 1
            
        print(f"\n게임 끝! {total}문제 중 {correct}개 맞추셨어요!")
        return correct, total

# 프로그램 실행
if __name__ == "__main__":
    game = EnglishLearningGame("멋쟁이씨")
    game.letter_distinction_game()  