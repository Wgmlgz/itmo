<script lang="ts">
  import { DataTable, TabContent } from 'carbon-components-svelte';
  import type {
    DataTableHeader,
    DataTableRow
  } from 'carbon-components-svelte/types/DataTable/DataTable.svelte';

  // Заголовки на основе предоставленного изображения
  let headers: DataTableHeader[] = [
    { key: 'id', value: 'ID' },
    { key: 'description', value: 'Description' },
    { key: 'detected', value: 'Detected' },
    { key: 'ack', value: 'ACK' },
    { key: 'suggestion', value: 'Suggestion' }
    // Добавьте остальные заголовки по образцу
  ];

  // Примерные данные для таблицы
  let rows: DataTableRow[] = [];

  // Генерация данных для таблицы
  // Это примерное наполнение, вам нужно будет подготовить реальные данные

  for (let i = 0; i < 1000; i++) {
    rows.push({
      id: i,
      description: 'Description for SPV' + i,
      detected: 'With sign of Minor',
      ack: i % 2 === 0 ? 'Yes' : 'No',
      suggestion: 'Example suggestion ' + i
      // Добавьте другие поля данных по образцу
    });
  }

  // setInterval(() => {
  const r = Math.round(Math.random() * 100) / 100;
  for (let i = 0; i < 1000; i++) {
    rows[i] = {
      id: i,
      description: `Description for SPV ${r}` + i,
      detected: 'With sign of Minor',
      ack: i % 2 === 0 ? 'Yes' : 'No',
      suggestion: `Example suggestion ${r} ` + i
      // Добавьте другие поля данных по образцу
    };
  }
  rows = rows;
  // }, 100);
</script>

<div class="w-full h-full p-4">
  <DataTable class="data-table" {rows} {headers} size="short" stickyHeader />
</div>

<style>
  /* Стили для таблицы */
  /* .data-table {
    font-size: 0.875rem; 
  }
  .data-table th {
    background-color: #f4f4f4;
    color: #000; 
    white-space: nowrap;
  }
  .data-table td {
    padding: 0.5rem;
    border-bottom: 1px solid #e0e0e0;
  }
  .data-table .bx--data-table-header {
    padding: 1rem; 
  } 
*/
  :global(.data-table .bx--data-table) {
    max-height: 650px;
  }
</style>
