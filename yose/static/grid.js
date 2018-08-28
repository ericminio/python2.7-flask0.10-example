Vue.component('grid', {
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
    methods: {
        play: function(line, column) {
            var id = 'cell-' + line + 'x' + column; 
            document.getElementById(id).className = 'cell lost'
        }
    }
})

load = function() {
}