/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/03 20:35:30 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/03 22:17:02 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putchar(char c)
{
	write(1, &c, 1);
}

int main()
{
	int a = 0;
	int b = 0;

	while(a < 3)
	{
			b = 0;
			while (b < 3)
			{
				ft_putchar('A');
				b++;
			}
			b = 0;
			while (b < 3)
			{
				ft_putchar('B');
				b++;
			}
			ft_putchar('\n');

		a++;
	
	}

	return (0);
}
