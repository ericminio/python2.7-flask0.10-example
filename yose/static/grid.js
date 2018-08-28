Vue.component('grid', {
    props: ['size'],
    template: `
        <div>
            <table>
                <tbody>
                    <tr v-for="line in size">
                        <td class="cell" v-for="column in size" v-on:click="play(line, column)">
                            <span v-bind:id="'cell-'+line+'x'+column">&nbsp;</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    `,
    methods: {
        play: function(line, column) {
            var id = 'cell-' + line + 'x' + column; console.log(id);    
            document.getElementById(id).className = 'lost'
        }
    }
})

load = function() {

}

