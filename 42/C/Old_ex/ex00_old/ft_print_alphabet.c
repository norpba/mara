/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/30 20:42:11 by hniinima          #+#    #+#             */
/*   Updated: 2022/06/30 21:56:57 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_putchar(char c);

void	ft_print_alphabet(void)

{
	int	i;

	i = 97;
	while (i <= 122)
	{
		ft_putchar(i);
		i++;
	}
}
