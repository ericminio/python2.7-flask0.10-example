let fs = require('fs');
let grid = fs.readFileSync('yose/static/grid.js').toString();
let source = `
    let Vue = {
        extend: function(options) { return options.methods; }
    };
    `
    + grid + ' return grid;';
let sut = (new Function(source))();

const jsdom = require("jsdom");
const { JSDOM } = jsdom;
let expect = require('chai').expect;

describe('play', ()=>{

    it('can be invoked', ()=>{
        var document = new JSDOM(`
            <html>
                <body>
                    <div id="cell-1x1"></div>
                </body>
            </html>`).window.document;
        document.grid = [
            [ 'empty', 'bomb' ]
        ];
        sut.digest(document);
        sut.play(1, 1);
        let cell = document.getElementById('cell-1x1');

        expect(cell.className).to.equal('cell safe surrounded-by-1');
    });
});