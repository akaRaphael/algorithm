package java_ds.javaSet;

import java_ds.interfaceImpl.SetInterface;

public class LinkedHashSet<E> implements SetInterface<E> {

    static class Node<E> {
        final int hash;
        final E key;

        Node<E> next; // separate chaining, 동일한 hash 값을 가진 다음 노드를 가리킴
        Node<E> nextLink; // 다음 노드 (입력순서보장 목적)
        Node<E> prevLink; // 이전 노드 (입력순서보장 목적)

        public Node(int hash, E key, Node<E> next) {
            this.hash = hash;
            this.key = key;
            this.next = next;

            this.nextLink = null;
            this.prevLink = null;

        }
    }

    // 여기서부터 Linked HashSet 구현부

    private final static int DEFAULT_CAPACITY = 1 << 4;
    private static final float LOAD_FACTOR = 0.75f;

    Node<E>[] table; // HashTable
    private int size; // HashTable 내부 요소의 개수

    private Node<E> head;
    private Node<E> tail;

    @SuppressWarnings("unchecked")
    public LinkedHashSet() {
        table = (Node<E>[]) new Node[DEFAULT_CAPACITY];
        size = 0;
        head = null;
        tail = null;
    }

    // 보조 해시 함수 (상속 방지를 위해 private static final 선언)
    private static final int hash(Object key) {
        int hash;
        if (key == null) {
            return 0;
        }
        else {
            // hashCode()에서 음수가 나오는 경우, 절대값으로 계산하여 양수로 만듬
            return Math.abs(hash = key.hashCode()) ^ (hash >>> 16);
        }
    }

    // 새로운 노드 추가
    private void linkLastNode(Node<E> newNode) {
        Node<E> last = tail;
        tail = newNode;

        if (last == null) { // 마지막 노드가 null 이라면 head 또한 null 이다.
            head = newNode;
        } else {
            newNode.prevLink = last;
            last.nextLink = newNode;
        }
    }

    @Override
    public boolean add(E data) {
        return add(hash(data), data) == null;
    }

    private E add(int hash, E key) {
        int idx = hash % table.length;
        Node<E> newNode = new Node<E>(hash, key, null);

        if(table[idx] == null) { // HashTable의 해당 index가 비어있는 경우, 새로운 노드를 저장
            table[idx] = newNode;
        }
        else { // HashTable의 해당 index에 이미 노드가 존재하면, 다음 노드가 없을 때까지 탐색 후 저장
            Node<E> temp = table[idx];
            Node<E> prev = null;

            while(temp != null) {
                // 동일한 digest와 key(저장 데이터)를 가진 노드가 존재한다면 중복이므로 저장할 필요가 없음
                if((temp.hash == hash) && (temp.key == key || temp.key.equals(key))) {
                    return key; // data를 반환함. 즉, 저장 안함
                }

                prev = temp;
                temp = temp.next;
            }

            prev.next = newNode;

        }

        size++;
        linkLastNode(newNode);

        if(size >= LOAD_FACTOR * table.length) {
            resize();
        }

        return null;
    }

    @SuppressWarnings("unchecked")
    private void resize() {

        int newCapacity = table.length * 2;
        final Node<E>[] newTable = (Node<E>[]) new Node[newCapacity]; // 기존 테이블의 두배 용적으로 생성

        for (int i = 0; i < table.length; i++) { // 0번째 index부터 차례대로 순회

            Node<E> value = table[i]; // 각 인덱스의 첫 번째 노드(head)

            if (value == null) { // 해당 값이 없을 경우 다음으로 넘어간다.
                continue;
            }

            table[i] = null;
            Node<E> nextNode;	// 현재 노드의 다음 노드를 가리키는 변수

            while (value != null) {// 현재 인덱스에 연결 된 노드들을 순회한다.

                int idx = value.hash % newCapacity;	// 새로운 인덱스를 구한다.

                // 해시충돌 => HashTable의 해당 index에 이미 노드가 존재하는 경우
                if (newTable[idx] != null) {
                    Node<E> tail = newTable[idx];

                    while (tail.next != null) { // 해당 index의 노드를 타고 마지막까지 탐색
                        tail = tail.next;
                    }

                    // table의 길이가 달라졌으므로 새롭게 매핑해줘야한다.
                    nextNode = value.next; // nextNode = 현재 index에 들어있는 Head의 다음 노드의 위치를 담는다.
                    value.next = null; // 현재 index의 head 의 다음 노드위치를 제거한다.
                    tail.next = value; // 새로운 HashTable의 위치에 head를 저장한다.
                }
                else { // 해쉬충돌 없는 경우 => HashTable의 해당 index가 빈 공간
                    nextNode = value.next;
                    value.next = null;
                    newTable[idx] = value;
                }
                value = nextNode; // 다음 노드로 이동
            }
        }
        table = null;
        table = newTable; // 기존의 HashTable을 새로운 HashTable로 교체
    }

    // 노드 삭제를 위한 연결 끊기
    private void unlinkNode(Node<E> targetNode) {
        Node<E> prevNode = targetNode.prevLink;	// 삭제하는 노드의 prev
        Node<E> nextNode = targetNode.nextLink;	// 삭제하는 노드의 next

        if (prevNode == null) { // 이전 노드가 없다 == 삭제할 노드가 head
            head = nextNode;
        }
        else {
            prevNode.nextLink = nextNode;
            targetNode.prevLink = null;
        }

        if (nextNode == null) { // 다음 노드가 없다 == 삭제할 노드가 tail
            tail = prevNode;
        }
        else {
            nextNode.prevLink = prevNode;
            targetNode.nextLink = null;
        }
    }

    @Override
    public boolean remove(Object data) {
        return remove(hash(data), data) != null; // null이 아니라면 노드가 삭제되었다는 것
    }

    private Object remove(int hash, Object key) {

        int idx = hash % table.length;
        Node<E> node = table[idx];
        Node<E> removedNode = null;
        Node<E> prev = null;

        if (node == null) {
            return null;
        }

        while (node != null) {
            // digest와 내용(key)이 같은 노드를 찾은 경우
            if (node.hash == hash && (node.key == key || node.key.equals(key))) {

                removedNode = node; // 삭제되는 노드를 반환하기 위해 담아두는 객체

                if (prev == null) { // prev가 없다는 것은 해당 index의 첫번째 head 노드라는 것
                    table[idx] = node.next;
                }
                else { // 삭제할 노드의 prev와 next를 연결한다.
                    prev.next = node.next;
                }

                unlinkNode(node); // HashTable의 체인을 끊었으니 순서를 유지하는 link를 끊는다.
                node = null;

                size--;
                break;	// HashTable에서 삭제되었으므로 종료
            }
            prev = node;
            node = node.next;
        }

        return removedNode;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public boolean contains(Object data) { // 노드 객체가 가진 데이터를 비교하여 존재여부를 파악한다.
        int idx = hash(data) % table.length;
        Node<E> temp = table[idx];

        while (temp != null) { // hash가 달라도 상관없다. 노드가 가진 값을 비교한다.
            if (data == temp.key || (data != null && temp.key.equals(data))) {
                return true;
            }
            temp = temp.next;
        }
        return false;
    }

    @Override
    public void clear() {
        if (table != null && size > 0) {
            for (int i = 0; i < table.length; i++) {
                table[i] = null;
            }
            size = 0;
        }
        head = tail = null;
    }
}
