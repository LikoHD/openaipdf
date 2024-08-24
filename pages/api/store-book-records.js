import { createClient } from '@supabase/supabase-js'

export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ message: '只允许POST请求' });
    }

    const { file_name, file_type, word_count, page_count, books } = req.body;

    const supabase = createClient(
        process.env.NEXT_PUBLIC_SUPABASE_URL,
        process.env.SUPABASE_SERVICE_ROLE_KEY
    );

    try {
        // 插入查询记录
        const { data: queryRecord, error: queryError } = await supabase
            .from('query_records')
            .insert({
                file_name,
                file_type,
                word_count,
                page_count,
                total_books_mentioned: Object.keys(books).length
            })
            .single();

        if (queryError) throw queryError;

        // 插入结果明细
        const resultDetails = Object.entries(books).map(([book_name, data]) => ({
            query_id: queryRecord.id,
            book_name,
            mention_count: data.count,
            pages: data.pages.join(',')
        }));

        const { data: detailsData, error: detailsError } = await supabase
            .from('result_details')
            .insert(resultDetails);

        if (detailsError) throw detailsError;

        res.status(200).json({ message: '数据成功存储到数据库' });
    } catch (error) {
        console.error('存储数据时出错:', error);
        res.status(500).json({ message: '存储数据时出错', error: error.message });
    }
}