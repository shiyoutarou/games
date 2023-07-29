const board = document.getElementById('board');
const cells = [];
const EMPTY = 0;
const BLACK = 1;
const WHITE = 2;

let currentPlayer = BLACK;
let gameOver = false;

function createCell(row, col) {
  const cell = document.createElement('div');
  cell.classList.add('cell');
  cell.dataset.row = row;
  cell.dataset.col = col;
  cell.addEventListener('click', () => handleCellClick(row, col));
  return cell;
}

function initializeBoard() {
  for (let row = 0; row < 15; row++) {
    for (let col = 0; col < 15; col++) {
      const cell = createCell(row, col);
      cells.push(cell);
      board.appendChild(cell);
    }
  }
}

function checkWin(row, col) {
  const directions = [
    [1, 0],
    [0, 1],
    [1, 1],
    [1, -1]
  ];

  for (const [dr, dc] of directions) {
    let count = 1;
    for (let step = 1; step <= 4; step++) {
      const newRow = row + dr * step;
      const newCol = col + dc * step;
      if (newRow < 0 || newRow >= 15 || newCol < 0 || newCol >= 15) break;
      if (cells[newRow * 15 + newCol].classList.contains(currentPlayer === BLACK ? 'black' : 'white')) {
        count++;
      } else {
        break;
      }
    }
    for (let step = -1; step >= -4; step--) {
      const newRow = row + dr * step;
      const newCol = col + dc * step;
      if (newRow < 0 || newRow >= 15 || newCol < 0 || newCol >= 15) break;
      if (cells[newRow * 15 + newCol].classList.contains(currentPlayer === BLACK ? 'black' : 'white')) {
        count++;
      } else {
        break;
      }
    }
    if (count >= 5) {
      gameOver = true;
      setTimeout(() => alert(`Player ${currentPlayer === BLACK ? 'Black' : 'White'} wins!`), 100);
      return;
    }
  }
}

function handleCellClick(row, col) {
  if (gameOver) return;

  const index = row * 15 + col;
  if (cells[index].classList.contains('black') || cells[index].classList.contains('white')) return;

  cells[index].classList.add(currentPlayer === BLACK ? 'black' : 'white');
  checkWin(row, col);

  currentPlayer = currentPlayer === BLACK ? WHITE : BLACK;
}

initializeBoard();
