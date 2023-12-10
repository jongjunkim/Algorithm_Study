def solution(genres, plays):
    
    genre_total_play = {}
    genre_songs = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total_play:
            genre_total_play[genre] = play
            genre_songs[genre] = [(i, play)]
        else:
            genre_total_play[genre] += play
            genre_songs[genre].append((i, play))
    
    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    
    result = [] 
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: x[1], reverse=True)[:2]
        result.extend(song[0] for song in songs)
    
    return result

#Hashmap을 역순으로 sort하기
#sorted_hashmap = sorted(hashmap.items(), lambda x:x[1], reverse = True)
#genre_total_play.items() 여기서 items()를 붙이는거는 Hashmap 전체를 하는거기떄문에
#genre_songs[genre] items() 안붙이는거는 Hashmap에 key에 해당하는 list를 하는거기떄문에 
# song[0] for song in songs 여기서 song[0] 이거는 song이 [(0, 500), (2, 150), (3, 800)] 형식으로 되어있기때문에 list에서 앞에 있는 숫자를 가져오기 위해
