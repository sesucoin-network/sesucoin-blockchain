const sesucoin = require('../../util/sesucoin');

describe('sesucoin', () => {
  it('converts number mojo to sesucoin', () => {
    const result = sesucoin.mojo_to_sesucoin(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to sesucoin', () => {
    const result = sesucoin.mojo_to_sesucoin('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to sesucoin string', () => {
    const result = sesucoin.mojo_to_sesucoin_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to sesucoin string', () => {
    const result = sesucoin.mojo_to_sesucoin_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number sesucoin to mojo', () => {
    const result = sesucoin.sesucoin_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string sesucoin to mojo', () => {
    const result = sesucoin.sesucoin_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = sesucoin.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = sesucoin.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = sesucoin.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = sesucoin.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = sesucoin.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = sesucoin.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
