import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as SesucoinIcon } from './images/sesucoin.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={SesucoinIcon} viewBox="0 0 58 58" {...props} />;
}
