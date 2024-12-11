public record Invoice
{
    public string InvoiceId { get; set; }
    public int Qty { get; set; }
    public string? Description { get; set; }
}