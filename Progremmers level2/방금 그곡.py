def solution(m, musicinfos):
    
    res = "(None)"
    interval = 0
    m = m.replace("C#","H").replace("D#", "I").replace("F#", "J").replace("G#","K").replace("A#", "L")
    
    for info in musicinfos:
        start, end, name, note = info.split(",")
        shr, smin = start.split(":")
        ehr, emin = end.split(":")
        start_minutes = int(shr)* 60 + int(smin)
        end_minutes = int(ehr)* 60 + int(emin)
        time = end_minutes - start_minutes
        note = note.replace("C#","H").replace("D#", "I").replace("F#", "J").replace("G#","K").replace("A#", "L")
        
        note = note * (time // len(note)) + note[0:time % len(note)]
         
        if m in note and interval < time:
            res = name
            interval = end_minutes - start_minutes
            
    return res

#나머지 부분은 정답과 비슷했으나 C# D#이거를 다른 단어로 대체 하는거 
# 그리고 note의 길이를 저렇게 time을 이용해서 하는것
