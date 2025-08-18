const Kata = require('./kata');

let fixture;

// This is a Jest unit test - see https://jestjs.io/docs/en/getting-started for more information

beforeEach(() => {
    fixture = new Kata();
});

test('hello should return message with specified name', () => {
    const name = 'Ingage';
    expect(fixture.hello(name)).toEqual(`Hello ${name}`);
});
