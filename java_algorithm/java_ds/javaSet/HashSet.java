package java_ds.javaSet;

import java.util.Arrays;

import java_ds.interfaceImpl.SetInterface;

public class HashSet<E> implements SetInterface<E> {

  class Node<E> {
    final int hash;
    final E key;
    Node<E> next;

    public Node(int hash, E key, Node<E> next) {
      this.hash = hash;
      this.key = key;
      this.next = next;
    }
  }

  // 기본 크기를 2^n 승의 단위로 설정한다.
  private final static int DEFAULT_CAPACITY = 1 << 4;

  // 배열의 3/4 이상 채워지는 경우 resize를 해야하므로, 이를 검증하기 위한 상수
  private final static float LOAD_FACTOR = 0.75f;

  Node<E>[] table; // node를 저장할 배열이므로 Node 타입으로 설정 
  private int size;

  @SuppressWarnings("unchecked")
	public HashSet() {
		table = (Node<E>[]) new Node[DEFAULT_CAPACITY];	
		size = 0;
	}
 
 
	// 상속 방지
	private static final int hash(Object key) {
		int hash;
		if (key == null) {
			return 0;
		} else {
			return Math.abs(hash = key.hashCode()) ^ (hash >>> 16);
		}
	}
 
	@SuppressWarnings("unchecked")
	private void resize() {
	
		int newCapacity = table.length * 2;
		
		// 기존 테이블의 두배 용적으로 생성
		final Node<E>[] newTable = (Node<E>[]) new Node[newCapacity];
 
		// 0번째 index부터 차례대로 순회
		for (int i = 0; i < table.length; i++) {
			Node<E> value = table[i];
 
			// 해당 값이 없을 경우 다음으로 넘어간다.
			if (value == null) {
				continue;
			}
 
			// capacity always 2^n
			/*
			 * hash 값은 동일하기 때문에 다시 계산할 필요 없으며 
			 * next가 없을 경우 value를 그대로 담으면 됨
			 */
			table[i] = null; // gc
 
			Node<E> nextNode;	// 현재 노드의 다음 노드를 가리키는 변수
			
			// 현재 인덱스에 연결 된 노드들을 순회한다.
			while (value != null) {
 
				int idx = value.hash % newCapacity;	// 새로운 인덱스를 구한다.
 
				/*
				 * 새로 담을 index에 요소(노드)가 존재할 경우
				 * == 새로 담을 newTalbe에 index값이 겹칠 경우 (해시 충돌)
				 */
				if (newTable[idx] != null) {
					Node<E> tail = newTable[idx];
 
					// 가장 마지막 노드로 간다. 
					while (tail.next != null) {
						tail = tail.next;
					}
					/*
					 *  반드시 value가 참조하고 있는 다음 노드와의 연결을 끊어주어야 한다.
					 *  안하면 각 인덱스의 마지막 노드(tail)도 다른 노드를 참조하게 되어버려
					 *  잘못된 참조가 발생할 수 있다.
					 */
					nextNode = value.next;
					value.next = null;
					tail.next = value;
				} 
				// 충돌되지 않는다면(=빈 공간이라면 해당 노드를 추가)
				else {
					
					/*
					 *  반드시 value가 참조하고 있는 다음 노드와의 연결을 끊어주어야 한다.
					 *  안하면 각 인덱스의 마지막 노드(tail)도 다른 노드를 참조하게 되어버려
					 *  잘못된 참조가 발생할 수 있다.
					 */
					nextNode = value.next;
					value.next = null;
					newTable[idx] = value;
				}
 
				value = nextNode;	// 다음 노드로 이동
			}
		}
		table = null;
		table = newTable;	// 새로 생성한 table을 table변수에 연결
	
 
	}
 
	@Override
	public boolean add(E e) {
		return add(hash(e), e) == null;
	}
 
	private E add(int hash, E key) {
 
	
		int idx = hash % table.length; // hash & (table.length - 1);
 
		// table[idx] 가 비어있을 경우 새 노드 생성
		if (table[idx] == null) {
			table[idx] = new Node<E>(hash, key, null);
		}
		
		/*
		 *  talbe[idx]에 요소가 이미 존재할 경우(==해시충돌)
		 *  
		 *  두 가지 경우의 수가 존재
		 *  1. 객체가 같은 경우
		 *  2. 객체는 같지 않으나 얻어진 index가 같은 경우
		 */
		else {
 
			Node<E> temp = table[idx];
			Node<E> prev = null;
			
			
			//  첫 노드(table[idx])부터 탐색한다.
			while (temp != null) {
 
				/*
				 *  만약 현재 노드의 객체가 같은경우는 
				 *  HashSet은 중복을 허용하지 않으므로 key를 반납(반환)
				 */
				if (temp.key.equals(key)) {
					return key;
				}
				prev = temp;
				temp = temp.next;
			}
 
			// 마지막 노드에 새 노드를 연결해준다.
			prev.next = new Node<E>(hash, key, null);
		}
		size++;
 
		// 데이터의 개수가 현재 table 용적의 75%을 넘어가는 경우 용적을 늘려준다.  
		if (size >= LOAD_FACTOR * table.length) {
			resize();
		}
		return null;	// 정상적으로 추가되었을 경우 null반환
	}
	
	@Override
	public boolean remove(Object o) {
		// null이 아니라는 것은 노드가 삭제되었다는 의미다.
		return remove(hash(o), o) != null;
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
			// 같은 노드를 찾았다면
			if(node.hash == hash && (node.key == key || node.key.equals(key))) {
				
				removedNode = node; //삭제되는 노드를 반환하기 위해 담아둔다.
				
				// 해당노드의 이전 노드가 존재하지 않는 경우 (= head노드인 경우)
				if (prev == null) {
					table[idx] = node.next;
					node = null;
				} 
				// 그 외엔 이전 노드의 next를 삭제할 노드의 다음노드와 연결해준다.
				else {
					prev.next = node.next;
					node = null;
				}
				size--;
				break;
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
	public boolean contains(Object o) {
		int idx = hash(o) % table.length;
		Node<E> temp = table[idx];
 
		/*
		 *  같은 객체 내용이어도 hash값은 다를 수 있다.
		 *  하지만, 내용이 같은지를 알아보고 싶을 때 쓰는 메소드이기에
		 *  hash값은 따로 비교 안해주어도 큰 지장 없다.  
		 *  단, o가 null인지는 확인해야한다.
		 */
		while (temp != null) {
			if ( o == temp.key || ( o != null && (o.equals(temp.key)))) {
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
	}
 
	
	@SuppressWarnings("unchecked")
	@Override
	public boolean equals(Object o) {
		
		// 만약 파라미터 객체가 현재 객체와 동일한 객체라면 true
		if(o == this) {
			return true;
		}
		// 만약 o 객체가 HashSet 이 아닌경우 false
		if(!(o instanceof HashSet)) {
			return false;
		}
		
		HashSet<E> oSet;
		
		/*
		 *  Object로부터 HashSet<E>로 캐스팅 되어야 비교가 가능하기 때문에
		 *  만약 캐스팅이 불가능할 경우 ClassCastException 이 발생한다.
		 *  이 경우 false를 return 하도록 try-catch문을 사용해준다.
		 */
		try {
			
			// HashSet 타입으로 캐스팅
			oSet = (HashSet<E>) o;
			// 사이즈(요소 개수)가 다르다는 것은 명백히 다른 객체다.
			if(oSet.size() != size) {
				return false;
			}
			
			for(int i = 0; i < oSet.table.length; i++) {
				Node<E> thisTable = table[i];
				Node<E> oTable = oSet.table[i];
								
				while(thisTable != null || oTable != null) {
					if(thisTable.key != oTable.key || !thisTable.key.equals(oTable.key)) {
						return false;
					}
					thisTable = thisTable.next;
					oTable = oTable.next;
				}
			}
			
		} catch(ClassCastException e) {
			return false;
		}
		return true;
 
	}
 
	public Object[] toArray() {
 
		if (table == null) {
			return null;
		}
		Object[] ret = new Object[size];
		int index = 0;	// 인덱스 변수를 따로 둔다.
 
		for (int i = 0; i < table.length; i++) {
 
			Node<E> node = table[i];
 
			// 해당 인덱스에 연결 된 모든 노드를 하나씩 담는다.
			while (node != null) {
				ret[index] = node.key;
				index++;
				node = node.next;
			}
		}
 
		return ret;
	}
 
	@SuppressWarnings("unchecked")
	public <T> T[] toArray(T[] a) {
 
		Object[] copy = toArray();	// toArray()통해 먼저 배열을 얻는다.
		
		// 들어온 배열이 copy된 요소 개수보다 작을경우 size에 맞게 늘려주면서 복사한다.
		if (a.length < size)
			return (T[]) Arrays.copyOf(copy, size, a.getClass());
 
		// 그 외에는 copy 배열을 a에 0번째부터 채운다.
		System.arraycopy(copy, 0, a, 0, size);
 
		return a;
	}
 
}