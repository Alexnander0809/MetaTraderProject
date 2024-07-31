using Microsoft.EntityFrameworkCore;
using MetaTraderAPI.Models;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

    public DbSet<AccountInfo> AccountInfos { get; set; }
}
