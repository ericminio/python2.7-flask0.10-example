var grid = Vue.extend({
    props: ['size'],
    template: `
        <div>
            <table>
                <tbody>
                    <tr v-for="line in size">
                        <td v-for="column in size" 
                            v-on:click="play(line, column)"
                            v-bind:id="'cell-'+line+'x'+column"
                            class="cell"
                        ></td>
                    </tr>
                </tbody>
            </table>
        </div>
    `,
    data: function() {
        return {
            cells: []
        };
    },
    methods: {
        digest: function(cells) {
            this.cells = cells;            
        },
        play: function(line, column) {
            var id = 'cell-' + line + 'x' + column; 
            var cell = document.getElementById(id);
            if (column == 1) {
                cell.className = 'cell safe surrounded-by-1';
                cell.innerHTML = '' + this.cells.length
            }
            else {
                cell.className = 'cell lost';
                cell.innerHTML = '';
            }
        }
    }
})


