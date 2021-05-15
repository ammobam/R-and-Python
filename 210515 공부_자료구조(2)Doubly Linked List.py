# 이중 연결 리스트
'''
단일 연결 리스트는 head 방향으로만 데이터를 삽입, 삭제, 조회함
이중 연결 리스트는 양방향 이동을 구현
- 노드 이동: next, prev
- 노드 양 끝: head, tail
'''
class DLinkedList:
    class Node:    # 노드 생성
        def __init__(self, v, n=None, p=None):
            self.value = v
            self.next = n
            self.prev = p
    def __init__(self): # 변수 설정
        self.head = None
        self.tail = None

    # 새로운 데이터 저장하기
    def insertNodeBefore(self, v):
        if self.head is None:
            self.head = self.Node(v)
            self.tail = self.head
        else:
            self.head.prev = self.Node(v, n=self.head)    # 새값받고, 기존값 next로 넘김
            self.head = self.head.prev  # 이동    # 기존노드의 prev는 새로운 노드임

    def insertNodeAfter(self, v):
        if self.tail is None:
            self.tail = self.Node(v)
            self.head = self.tail
        else:
            self.tail.next = self.Node(v, p=self.tail)
            self.tail = self.tail.next

    # 출력: head부터
    def printNodeBefore(self):
        if self.head is None:
            print("head에 저장된 데이터가 없습니다")
            return
        else:
            link = self.head
            print("현재 리스트 구조:", end="\t")
            while link:
                print(link.value, "<->", end=" ")
                link = link.next
            print()
    # 출력: tail부터
    def printNodeAfter(self):
        if self.tail is None:
            print("tail에 저장된 데이터가 없습니다")
            return
        else:
            link = self.tail
            print("현재 리스트 구조:", end="\t")
            while link:
                print(link.value, "<->", end=" ")
                link = link.prev
            print()
    # 삭제
    ## 저장된 노드가 있을 때 처리가 싱글 링크 리스트와 달라짐
    ## head로 삭제
    def deleteNodeBefore(self):
        if self.head is None:
            print("삭제할 데이터가 없습니다")
            return
        else:
            self.head = self.head.next
            self.head.prev = None   # 단일 노드 때는 왜 안 했지?

    ## tail로 삭제
    def deleteNodeAfter(self):
        if self.tail is None:
            print("삭제할 데이터가 없습니다")
            return
        else:
            self.tali = self.tail.prev
            self.tail.next = None   # 단일 노드 때는 왜 안 했지?







#------테스트------
if __name__=="__main__":
    dl = DLinkedList()
    dl.insertNodeBefore('1st')  # head삽입 테스트
    dl.insertNodeBefore('2nd')  # head삽입 테스트
    dl.insertNodeBefore('3rd')  # head삽입 테스트
    dl.insertNodeAfter('B1st') # tail삽입 테스트
    dl.insertNodeAfter('B2nd') # tail삽입 테스트
    dl.insertNodeAfter('B3rd') # tail삽입 테스트
    dl.printNodeBefore()
    dl.printNodeAfter()
    dl.deleteNodeBefore()  # head로 삭제
    dl.printNodeBefore()
    dl.deleteNodeAfter()  # tail로 삭제
    dl.printNodeBefore()