# Author: Abshar Mohammed Aslam, github.com/abxhr

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_index = []
        boxes = list(boxes)
        answer = []
        for i, box in enumerate(boxes):
            if box == '1':
                ball_index.append(i)
        for i in range(len(boxes)):
            answer.append(sum([abs(curr_pos-i) for curr_pos in ball_index]))
        return answer