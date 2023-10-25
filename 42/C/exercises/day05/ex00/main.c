/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/04 16:45:22 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/04 18:06:14 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putstr(char *c);

int main(void)
{
	char str[] = "Currently having psykoosi with C";
	char *strptr;

	strptr = &str[0];
	ft_putstr(strptr);
	return (0);
}
