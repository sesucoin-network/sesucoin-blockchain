import React from 'react';
import styled from 'styled-components';
import { Box, BoxProps } from '@material-ui/core';
import { Sesucoin } from '@sesucoin/icons';

const StyledSesucoin = styled(Sesucoin)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledSesucoin />
    </Box>
  );
}
