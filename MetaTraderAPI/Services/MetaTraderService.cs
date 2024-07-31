using System;
using System.Threading.Tasks;
using MetaTraderAPI.Models;
using MetaTraderAPI.Data;
using Microsoft.EntityFrameworkCore;

public class MetaTraderService
{
    private readonly ApplicationDbContext _context;
    private readonly string _login;
    private readonly string _password;
    private readonly string _server;

    public MetaTraderService(ApplicationDbContext context, string login, string password, string server)
    {
        _context = context;
        _login = login;
        _password = password;
        _server = server;
    }

    public async Task<AccountInfo> GetAccountInfoAsync()
    {
        // Implementa la lógica para conectarte a MetaTrader y obtener la información de la cuenta
        var manager = new MetaTrader5Manager(_server, _login, _password);

        if (!manager.Login())
        {
            throw new Exception("Error al iniciar sesión en MetaTrader");
        }

        var accountInfo = new AccountInfo
        {
            Balance = manager.GetBalance(),
            Equity = manager.GetEquity(),
            Margin = manager.GetMargin()
        };

        _context.AccountInfos.Add(accountInfo);
        await _context.SaveChangesAsync();

        return accountInfo;
    }

    public decimal CalculateNextMonthBalance(decimal currentBalance, decimal monthlyRate)
    {
        // Calcula el balance del siguiente mes
        return currentBalance * (1 + monthlyRate / 100);
    }
}
