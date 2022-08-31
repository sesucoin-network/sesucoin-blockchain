import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useSelector } from 'react-redux';
import type { RootState } from '../../../modules/rootReducer';
import FarmCard from './FarmCard';
import { mojo_to_sesucoin } from '../../../util/sesucoin';
import useCurrencyCode from '../../../hooks/useCurrencyCode';

export default function FarmCardTotalSesucoinFarmed() {
  const currencyCode = useCurrencyCode();

  const loading = useSelector(
    (state: RootState) => !state.wallet_state.farmed_amount,
  );

  const farmedAmount = useSelector(
    (state: RootState) => state.wallet_state.farmed_amount?.farmed_amount,
  );

  const totalSesucoinFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      const val = BigInt(farmedAmount.toString());
      return mojo_to_sesucoin(val);
    }
  }, [farmedAmount]);

  return (
    <FarmCard
      title={<Trans>Total Sesucoin Farmed</Trans>}
      value={totalSesucoinFarmed}
      loading={loading}
    />
  );
}
