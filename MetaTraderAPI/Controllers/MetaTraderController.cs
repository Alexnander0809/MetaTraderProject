using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using MetaTraderAPI.Services;

[Route("api/[controller]")]
[ApiController]
public class MetaTraderController : ControllerBase
{
    private readonly MetaTraderService _metaTraderService;

    public MetaTraderController(MetaTraderService metaTraderService)
    {
        _metaTraderService = metaTraderService;
    }

    [HttpGet("account-info")]
    public async Task<IActionResult> GetAccountInfo()
    {
        var accountInfo = await _metaTraderService.GetAccountInfoAsync();
        return Ok(accountInfo);
    }

    [HttpGet("next-month-balance")]
    public IActionResult GetNextMonthBalance(decimal currentBalance, decimal monthlyRate)
    {
        var nextMonthBalance = _metaTraderService.CalculateNextMonthBalance(currentBalance, monthlyRate);
        return Ok(nextMonthBalance);
    }
}
