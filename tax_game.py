# TaxHack Game
# Simple interactive script to calculate taxes, social contributions, and net income
# This is a toy example and not official tax advice.

import sys


def prompt(msg, cast_func=str):
    while True:
        try:
            return cast_func(input(msg))
        except Exception:
            print("Invalid input. Try again.")


def compute_taxes(status, gross_income, expenses, tesla=False):
    taxable_income = gross_income - expenses
    if tesla:
        tesla_price = 50000
        deduction = tesla_price * 0.8
        taxable_income -= deduction
    tax_rates = {
        "freelance": 0.20,
        "societe": 0.25,
        "salarie": 0.30,
    }
    social_rates = {
        "freelance": 0.15,
        "societe": 0.20,
        "salarie": 0.15,
    }
    tax = max(taxable_income, 0) * tax_rates.get(status, 0.25)
    social = max(taxable_income, 0) * social_rates.get(status, 0.15)
    net_income = gross_income - expenses - tax - social
    return tax, social, net_income


def main():
    print("=== TaxHack Simulation ===")
    status = prompt("Votre statut (freelance, societe, salarie) : ").strip().lower()
    gross = prompt("Revenu brut (€): ", float)
    depenses = prompt("Depenses (€): ", float)
    tesla_resp = prompt("Mode 'Et si j'achetais une Tesla ?' (o/n) : ").strip().lower()
    tesla = tesla_resp == 'o'

    tax, social, net = compute_taxes(status, gross, depenses, tesla)

    print("\n--- Resultats ---")
    if tesla:
        print("Simulation avec achat de Tesla")
    print(f"Impots: {tax:.2f} €")
    print(f"Cotisations sociales: {social:.2f} €")
    print(f"Revenu net: {net:.2f} €")


if __name__ == "__main__":
    main()
