# 프로그래머스 고득점 kit - hash
# 베스트 앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

# 입출력 예시
# 장르 / 횟수 / 결과 
# 장르 => ["classic", "pop", "classic", "classic", "pop"]
# 횟수 => [500, 600, 150, 800, 2500]
# 결과 => [4, 1, 3, 0]

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 내가 짠 코드 
def solution(genres, plays):
  
  # 각 장르별 총 플레이 횟수 계산 => 장르의 추출 순서를 알기 위함 
  sum_by_genre = list(zip(genres, plays))
  sum_dict = {}
  for genre, play in sum_by_genre:
    if genre in sum_dict.keys():
      sum_dict[genre] += play
    else:
      sum_dict[genre] = play
      
  sum_dict = sorted(sum_dict.items(), key = lambda x : x[1], reverse = True)
  
  # 총 플레이 횟수대로 장르의 추출 순서
  genre_order = []
  for category, count in sum_dict:
    genre_order.append(category)
  
  # 장르별로 가장 플레이 횟수가 많은 곡 2개씩 뽑기 
  idx = [i for i in range(len(genres))]
  play_list = list(zip(genres, plays, idx))
  play_list = sorted(play_list, key = lambda x : x[1], reverse = True)
  
  candidate_dict = {}
  for category, play, index in play_list:
    if category in candidate_dict.keys():
      if len(candidate_dict[category]) < 2:
        candidate_dict[category] += [index]
    else:
      candidate_dict[category] = [index]
      
  # 장르 순서에 맞게 합치기 
  answer = []
  for genre in genre_order:
    answer += candidate_dict[genre]
  
  return answer

print(solution(genres, plays))

# 다른 사람의 솔루션 
def solution2(genres, plays):
  answer = []
  play_dict = {}
  d = {}
  
  for i in range(len(genres)):
    genre = genres[i]
    play = plays[i]
    play_dict[genre] = play_dict.get(genre, 0) + play
    d[genre] = d.get(genre, []) + [(play, i)]
    
    genre_sort = sorted(play_dict.items(), key = lambda x : x[1], reverse = True)
    
  for genre, total in genre_sort:
    d[genre] = sorted(d[genre], key = lambda x: (-x[0], x[1]))
    answer += [idx for play, idx in d[genre][:2]]
      
  return answer
      