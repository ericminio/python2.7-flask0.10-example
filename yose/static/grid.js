Vue.component('grid', {
    props: ['size'],
    template: `
        <div>
            <table>
                <tbody>
                    <tr v-for="line in size">
                        <td class="cell" v-for="column in size">
                            <span v-bind:id="'cell-'+line+'x'+column"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    `   
})