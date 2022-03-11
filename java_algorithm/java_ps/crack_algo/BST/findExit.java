package java_ps.crack_algo.BST;


/**
 * https://www.youtube.com/watch?v=ht9QAfQpCnQ
 * 재귀함수 정복하기
 */

public class findExit {
    public boolean searchMaze(String[][] map, boolean[][] seen, int row, int col) {

        // 1. Base case 설정하기

        // a. 지도를 벗어난 경우
        if (row < 0 || row >= map.length || col < 0 || col >= map[0].length) {
            return false;
        }

        // b. 벽에 부딪히는 경우
        if (map[row][col] == "*") {
            return false;
        }

        // c. 이미 방문했던 위치인 경우
        if (seen[row][col]) {
            return false;
        }

        // d. 출구를 발견한 경우
        if (map[row][col] == "EXIT") {
            return true;
        }

        // 우선 현재 위치를 방문했음을 기록
        seen[row][col] = true;

        // 2. Recurse
        // 상하좌우 움직임을 구현

        return searchMaze(map, seen, row - 1, col) || // 위로 이동
                searchMaze(map, seen, row + 1 ,col) || // 아래로 이동
                searchMaze(map, seen, row, col - 1) || // 좌측으로 이동
                searchMaze(map,seen, row, col + 1); // 우측으로 이동
    }
}
