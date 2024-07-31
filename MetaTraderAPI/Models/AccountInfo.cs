namespace MetaTraderAPI.Models
{
    public class AccountInfo
    {
        public int Id { get; set; }
        public decimal Balance { get; set; }
        public decimal Equity { get; set; }
        public decimal Margin { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    }
}
