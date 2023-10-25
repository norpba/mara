/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/04 20:11:54 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/05 13:24:16 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char c);

void	ft_putnbr(int nbr)

{
	long lnbr = nbr;

	if (lnbr < 0)
	{
		ft_putchar('-');
		lnbr = -lnbr;
	}

	if (lnbr/10)
		ft_putnbr(lnbr/10);
	ft_putchar(lnbr%10 + '0');
}
